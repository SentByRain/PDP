from typing import Literal
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

# Pydantic-схема для данных пользователя
class UserCreate(BaseModel):
    name : str = Field(...)
    surname : str = Field(...)
    email : EmailStr = Field(...)
    password : str = Field(...)
    role : Literal['student', 'teacher'] = Field(...) 
    verification_code: str = Field(...)

class UserUpdate(BaseModel):
    email : EmailStr | None = None 
    old_password : str | None = None
    new_password : str | None = None
    verification_code: str = Field(...)

class UserGet(BaseModel):
    id : int
    name : str
    surname : str
    email : EmailStr
    password : str
    created_at : datetime

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., description="Пароль, от 5 до 50 знаков")


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: EmailStr | None = None


class UserSchema(BaseModel):
    id : int
    name : str
    surname : str
    email : EmailStr
    password : str

    is_user : bool = Field(default=True)
    is_student : bool = Field(default=False)
    is_teacher : bool = Field(default=False)
    is_admin : bool = Field(default=False)
    is_super_admin : bool = Field(default=False)


class UserInDB(UserSchema):
    hashed_password: str


