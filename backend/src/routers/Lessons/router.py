from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.config import CONFIG
from src.logger import logger

from src.models import LessonDAO, UserDAO
from src.database_control.db import get_db
from src.routers.Users.auth import get_current_user
from src.routers.Lessons.schemas import LessonSchema


PREFIX = '/lessons'

router = APIRouter(prefix=PREFIX, tags=['Lessons'])

@router.get('')
def get_lessons(user : UserDAO = Depends(get_current_user), 
                db : Session = Depends(get_db)) -> List[LessonSchema] | None:
    if user.is_student:
        lessons = db.query(LessonDAO).filter(LessonDAO.student_id == user.id).all()
    if user.is_teacher:
        lessons = db.query(LessonDAO).filter(LessonDAO.teacher_id == user.id).all()

    if lessons:
        return [LessonSchema(start_time=lesson.start_time,
                             end_time=lesson.end_time,
                             theme=lesson.theme,
                             lesson_description=lesson.lesson_description,
                             hw_description=lesson.hw_description,
                             teacher_id=lesson.teacher_id,
                             student_id=lesson.student_id,
                             status=lesson.status) 
                             for lesson in lessons]
    else: 
        raise HTTPException(404, "Lessons not found")
    
@router.post('/create')
def create_lesson(lesson : LessonSchema,
                  user : UserDAO = Depends(get_current_user), 
                  db : Session = Depends(get_db)) -> int:
    if user.is_student:
        raise HTTPException(403, "Forbidden")
    
    if user.is_teacher:
        lesson_dao = LessonDAO(**lesson.model_dump())
        db.add(lesson_dao)

    db.commit()

    db.refresh(lesson_dao)

    return lesson_dao.id

