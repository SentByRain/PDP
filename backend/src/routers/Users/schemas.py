from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

# Pydantic-схема для данных пользователя
class UserCreate(BaseModel):
    name : str = Field(...)
    surname : str = Field(...)
    email : EmailStr = Field(...)
    password : str = Field(...)
    verification_code: str = Field(...)

class UserUpdate(BaseModel):
    name: str | None = None  
    surname: str | None = None
    email : EmailStr | None = None 
    password : str | None = None

class UserGet(BaseModel):
    id : int
    name : str
    surname : str
    email : EmailStr
    password : str
    created_at : datetime

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков")
