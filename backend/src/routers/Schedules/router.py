
from enum import Enum
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.config import CONFIG
from src.logger import logger

from src.models import Schedule
from src.database_control.db import get_db

from src.routers.Schedules.schemas import LessonCreate, LessonDelete, LessonGet, LessonUpdate, Lesson


PREFIX = '/schedules'

router = APIRouter(prefix=PREFIX, tags=['Schedules'])

@router.post("/get/", response_model=Lesson)
def get_lesson(request: LessonGet, db: Session = Depends(get_db)):
    # Изменяем урок
    try:

        lesson = db.query(Schedule).filter(Schedule.teacher_id == request.teacher_id,
                                           Schedule.student_id == request.student_id,
                                           Schedule.start_time == request.start_time,
                                           Schedule.end_time == request.end_time).first()
        if lesson is None:
            raise HTTPException(status_code=404, detail="Lesson not found")
        

        return lesson
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))

@router.post("/create/")
def create_lesson(request: LessonCreate, db: Session = Depends(get_db)) -> str:
    # Создаём новый урок
    try:

        new_lesson = Schedule(teacher_id = request.teacher_id,
                            student_id = request.student_id,
                            start_time = request.start_time,
                            end_time = request.end_time,
                            status = request.status
                        )
        db.add(new_lesson)
        db.commit()

        return "The lesson was successfully created"
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))

@router.delete("/delete/")
def delete_lesson(request : LessonDelete, db: Session = Depends(get_db)) -> str:
    # Удаляем урок
    try:

        lesson = db.query(Schedule).filter(Schedule.teacher_id == request.teacher_id,
                                    Schedule.student_id == request.student_id,
                                    Schedule.start_time == request.start_time,
                                    Schedule.end_time == request.end_time).first()
        if lesson is None:
            raise HTTPException(status_code=404, detail="Lesson not found")
        
        db.delete(lesson)
        db.commit()

        return "The lesson was successfully deleted"
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))

@router.put("/change/")
def update_lesson(choosen_lesson: LessonGet, request: LessonUpdate, db: Session = Depends(get_db)) -> str:
    # Изменяем урок
    try:

        lesson = db.query(Schedule).filter(Schedule.teacher_id == choosen_lesson.teacher_id,
                                    Schedule.student_id == choosen_lesson.student_id,
                                    Schedule.start_time == choosen_lesson.start_time,
                                    Schedule.end_time == choosen_lesson.end_time).first()
        if lesson is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Update fields if provided
        if request.teacher_id is not None:
            lesson.teacher_id = request.teacher_id
        if request.student_id is not None:
            lesson.student_id = request.student_id
        if request.start_time is not None:
            lesson.start_time = request.start_time
        if request.end_time is not None:
            lesson.end_time = request.end_time
        if request.status is not None:
            lesson.status = request.status

        
        db.commit()
        db.refresh(lesson)  # Refresh to get updated data from the database

        return "The lesson was successfully updated"
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))
