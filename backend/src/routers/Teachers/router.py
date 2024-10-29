
from enum import Enum
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.config import CONFIG
from src.logger import logger

from src.models import Teacher
from src.database_control.db import get_db

from src.routers.Teachers.schemas import UserCreate, UserUpdate, UserGet


PREFIX = '/teachers'

router = APIRouter(prefix=PREFIX, tags=['Teachers'])

@router.get("/get/{email}", response_model=UserGet)
def get_user(email : str, db: Session = Depends(get_db)):
    # Изменяем пользователя
    try:

        user = db.query(Teacher).filter(Teacher.email == email).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        return user
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))

@router.post("/create/")
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> str:
    # Создаём нового пользователя
    try:

        new_user = Teacher(name=user.name, 
                        surname=user.surname, 
                        email=user.email, 
                        )
        db.add(new_user)
        db.commit()

        return new_user.email
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))

@router.delete("/delete/{email}")
def delete_user(email : str, db: Session = Depends(get_db)) -> str:
    # Удаляем пользователя
    try:

        user = db.query(Teacher).filter(Teacher.email == email).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        db.delete(user)
        db.commit()

        return user.email
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))

@router.put("/change/{email}")
def update_user(user_update: UserUpdate, email : str, db: Session = Depends(get_db)) -> str:
    # Изменяем пользователя
    try:

        user = db.query(Teacher).filter(Teacher.email == email).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
            # Update fields if provided
        if user_update.name is not None:
            user.name = user_update.name
        if user_update.surname is not None:
            user.surname = user_update.surname
        if user_update.email is not None:
            user.email = user_update.email
        
        db.commit()
        db.refresh(user)  # Refresh to get updated data from the database

        return user.email
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))
