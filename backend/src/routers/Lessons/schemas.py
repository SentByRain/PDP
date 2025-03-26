from typing import Literal
from pydantic import BaseModel
from datetime import datetime

# Pydantic-схема для данных пользователя
class LessonSchema(BaseModel):

    start_time : datetime
    end_time : datetime
    theme : str | None
    lesson_description : str | None
    hw_description : str | None
    teacher_id : int
    student_id : int
    status : Literal['active', 'passed', 'cancelled'] = 'active'
