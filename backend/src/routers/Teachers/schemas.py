from pydantic import BaseModel, EmailStr
from datetime import datetime

# Pydantic-схема для данных пользователя
class UserCreate(BaseModel):
    name : str
    surname : str
    email : EmailStr

class UserUpdate(BaseModel):
    name: str | None = None  # Optional fields
    surname: str | None = None
    email : EmailStr | None = None  # Optional fields

class UserGet(BaseModel):
    id : int
    name : str
    surname : str
    email : EmailStr
    created_at : datetime