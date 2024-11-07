
from fastapi import APIRouter, HTTPException
from pydantic import EmailStr

from src.routers.Mail.mail import send_confirmation_email




PREFIX = '/mail'


router = APIRouter(prefix=PREFIX, tags=['Mail'])


@router.post("/send_verification_code")
def update_user(email: EmailStr) -> str:
    # Изменяем пользователя
    try:
        
        send_confirmation_email(to_email=email)

        return email
    except Exception as e:
        raise HTTPException(500, detail=str(e))
