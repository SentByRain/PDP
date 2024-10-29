from typing import Literal
from pydantic import BaseModel, Field
from datetime import datetime

# Pydantic-схема для данных пользователя
class LessonCreate(BaseModel):
    teacher_id: int
    student_id: int
    start_time: datetime
    end_time: datetime
    status: Literal['active', 'pussed'] = Field(default='active')

class LessonUpdate(BaseModel):
    teacher_id: int | None
    student_id: int | None
    start_time: datetime | None
    end_time: datetime | None
    status: Literal['active', 'pussed'] | None = Field(default='active')

class LessonDelete(BaseModel):
    teacher_id: int 
    student_id: int 
    start_time: datetime 
    end_time: datetime

class LessonGet(BaseModel):
    teacher_id: int 
    student_id: int 
    start_time: datetime 
    end_time: datetime

class Lesson(BaseModel):
    id: int
    teacher_id: int 
    student_id: int 
    start_time: datetime 
    end_time: datetime
    status: Literal['active', 'pussed']
    created_at: datetime