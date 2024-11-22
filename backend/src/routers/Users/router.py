
from enum import Enum
from fastapi import FastAPI
from fastapi import APIRouter, HTTPException, Depends, status, Response
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager

from src.routers.Mail.mail import get_code
from src.logger import logger

from src.models import User
from src.database_control.db import get_db

from src.config import CONFIG
from src.routers.Users.schemas import UserCreate, UserUpdate, UserGet, UserAuth
from src.routers.Users.auth import (get_password_hash,  
                                    create_access_token, 
                                    authenticate_user,
                                    get_current_user,
                                    get_current_admin_user,
                                    verify_password)


PREFIX = '/users'

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = next(get_db())

    admin_user = User(name = 'admin', 
                      surname = 'admin', 
                      email = 'admin@mail.com', 
                      password = get_password_hash('admin'),
                      is_admin = True)
    
    db.add(admin_user)
    db.commit()
    yield

router = APIRouter(prefix=PREFIX, tags=['Users'], lifespan=lifespan)

@router.post("/register/")
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> str:
    # Создаём нового пользователя

    code = get_code(user.email)

    assert user.verification_code == code, f"Invalid verification code {user.verification_code} != {code}"
    
    try:
        check_user = db.query(User).filter(User.email == user.email).first()

        if  check_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Пользователь уже существует'
            )
        

        new_user = User(name=user.name, 
                        surname=user.surname, 
                        email=user.email, 
                        password=get_password_hash(user.password),
                        **CONFIG.ROLES_HASHMAP.get(user.role)
                        )
        db.add(new_user)
        db.commit()

        return new_user.email
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))
    

@router.post("/login/")
async def auth_user(response: Response, user_data: UserAuth, db: Session = Depends(get_db)):
    check = await authenticate_user(email=user_data.email, password=user_data.password, db=db)
    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверная почта или пароль')
    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}

@router.put("/change/")
def update_user(user_update: UserUpdate, db: Session = Depends(get_db)) -> str:
    # Изменяем пользователя
    try:
        print(user_update.email)

        user = db.query(User).filter(User.email == user_update.email).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        assert verify_password(plain_password=user_update.old_password, hashed_password=user.password), "Invalid old password"
        
        code = get_code(user.email)

        assert user_update.verification_code == code, f"Invalid verification code {user_update.verification_code} != {code}"
        
        user.password = get_password_hash(user_update.new_password)
        
        db.commit()
        db.refresh(user)  # Refresh to get updated data from the database

        return user.email
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))

@router.get("/me/")
async def get_me(user_data: User = Depends(get_current_user)):
    return user_data

@router.post("/logout/")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}

@router.get("/all_users/")
async def get_all_users(user_data: User = Depends(get_current_admin_user), db : Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/get/{email}", response_model=UserGet)
def get_user(email : str, user_data: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Изменяем пользователя
    try:

        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        return user
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))
    
@router.delete("/delete/{email}")
def delete_user(email : str, user_data: User = Depends(get_current_user), db: Session = Depends(get_db)) -> str:
    # Удаляем пользователя
    try:

        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        db.delete(user)
        db.commit()

        return user.email
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))


