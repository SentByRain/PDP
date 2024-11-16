
from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import EmailStr
from sqlalchemy.orm import Session

from src.routers.Mail.mail import send_confirmation_email
from src.models import User
from src.database_control.db import get_db




PREFIX = '/mail'


router = APIRouter(prefix=PREFIX, tags=['Mail'])


@router.post("/send_verification_code")
def send_post_code(email: EmailStr, db : Session = Depends(get_db)) -> str:

    try:
        check_user = db.query(User).filter(User.email == email).first()

        if  check_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Пользователь уже существует'
            )
        
        send_confirmation_email(to_email=email)

        return email
    except Exception as e:
        raise HTTPException(500, detail=str(e))
