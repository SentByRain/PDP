from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.config import CONFIG
from src.logger import logger

from src.models import HomeworkDAO, UserDAO, LessonDAO
from src.database_control.db import get_db
from src.routers.Users.auth import get_current_user
from src.routers.Homework.schemas import HomeworkSchema


PREFIX = '/homeworks'

router = APIRouter(prefix=PREFIX, tags=['Homeworks'])

def get_lesson_by_hw_id_and_user_id(user_id : int, 
                                    homework_id : int,
                                    db : Session):
    lesson = db.query(LessonDAO).filter(
        LessonDAO.hw_id == homework_id,
        LessonDAO.student_id == user_id
    ).first()
    return lesson


@router.get('/{id}')
def get_homework(user : UserDAO = Depends(get_current_user), 
                db : Session = Depends(get_db)) -> List[HomeworkSchema] | None:
    
    lesson = get_lesson_by_hw_id_and_user_id(user_id=user.id,
                                             homework_id=id,
                                             db=db)
    
    if not lesson:
        raise HTTPException(403, "Forbiden")

    homework = db.query(HomeworkDAO).filter(HomeworkDAO.id == id).first()

    return HomeworkSchema(files_urls=homework.files_urls,
                          answer=homework.answer,
                          sent_files=homework.sent_files,
                          deadline=homework.deadline)
    
# @router.post('/create')
# def create_lesson(homework : LessonSchema,
#                   user : User = Depends(get_current_user), 
#                   db : Session = Depends(get_db)) -> int:
#     if user.is_student:
#         raise HTTPException(403, "Forbidden")
    
#     if user.is_teacher:
#         lesson_dao = LessonDAO(**lesson.model_dump())
#         db.add(lesson_dao)

#     db.commit()

#     db.refresh(lesson_dao)

#     return lesson_dao.id

