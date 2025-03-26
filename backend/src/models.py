import enum
from typing import List
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Text, Table, UniqueConstraint, DateTime, Boolean, text, func, JSON
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserDAO(Base):
    __tablename__ = "users"

    id : Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = Column(String(36), nullable=False)
    surname : Mapped[str] = Column(String(36), nullable=False)
    email : Mapped[str] = Column(String, unique=True, nullable=False)
    password : Mapped[str] = Column(String, nullable=False)

    is_user : Mapped[bool] = Column(Boolean, default=True, server_default=text('true'), nullable=False)
    is_student : Mapped[bool] = Column(Boolean, default=False, server_default=text('false'), nullable=False)
    is_teacher : Mapped[bool] = Column(Boolean, default=False, server_default=text('false'), nullable=False)
    is_admin : Mapped[bool] = Column(Boolean, default=False, server_default=text('false'), nullable=False)
    is_super_admin : Mapped[bool] = Column(Boolean, default=False, server_default=text('false'), nullable=False)

    updated_at : Mapped[datetime] = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at : Mapped[datetime] = Column(DateTime, default=func.now())


class Shedule(Base):
    __tablename__ = "schedules"

    id : Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    lesson_id : Mapped[int] = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    user_id : Mapped[int] = Column(Integer, ForeignKey("users.id"), nullable=False)

    updated_at : Mapped[datetime] = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at : Mapped[datetime] = Column(DateTime, default=func.now())


class LessonDAO(Base):
    __tablename__ = "lessons"

    id : Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    start_time : Mapped[datetime] = Column(DateTime, nullable=False)
    end_time : Mapped[datetime] = Column(DateTime, nullable=False)
    theme : Mapped[str] = Column(String, nullable=True)
    lesson_description : Mapped[str] = Column(String, nullable=True)
    hw_description : Mapped[str] = Column(String, nullable=True)
    teacher_id : Mapped[int] = Column(Integer, nullable=False)
    student_id : Mapped[int] = Column(Integer, nullable=False)
    status : Mapped[str] = Column(String, nullable=False, default='active')

    hw_id : Mapped[int] = Column(Integer, ForeignKey("homeworks.id"), nullable=True)

    homework = relationship("HomeworkDAO", back_populates="lesson", uselist=False)

    updated_at : Mapped[datetime] = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at : Mapped[datetime] = Column(DateTime, default=func.now())

    __table_args__ = (UniqueConstraint("teacher_id", "student_id", "start_time", "end_time", name="_teacher_student_time_uc"),)


class HomeworkDAO(Base):
    __tablename__ = "homeworks"

    id : Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    files_urls : Mapped[List] = Column(JSON, nullable=True)
    answer : Mapped[str] = Column(String, nullable=True)
    sent_files : Mapped[List] = Column(JSON, nullable=True)
    deadline : Mapped[datetime] = Column(DateTime, nullable=True)

    lesson = relationship("LessonDAO", back_populates="homework", uselist=False)

    updated_at : Mapped[datetime] = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at : Mapped[datetime] = Column(DateTime, default=func.now())



class Dialog(Base):
    __tablename__ = "dialogs"

    id : Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    teacher_id : Mapped[int] = Column(Integer, nullable=False)
    student_id : Mapped[int] = Column(Integer, nullable=False)
    conversation_id : Mapped[int] = Column(Integer, ForeignKey("conversations.id"), nullable=False)

    updated_at : Mapped[datetime] = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at : Mapped[datetime] = Column(DateTime, default=func.now())


class Conversation(Base):
    __tablename__ = "conversations"

    id : Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    message_id : Mapped[int] = Column(Integer, ForeignKey("messages.id"), nullable=False)

    updated_at : Mapped[datetime] = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at : Mapped[datetime] = Column(DateTime, default=func.now())


class Message(Base):
    __tablename__ = "messages"

    id : Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    text : Mapped[str] = Column(String, nullable=True)
    file_url : Mapped[str] = Column(String, nullable=True)

    updated_at : Mapped[datetime] = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at : Mapped[datetime] = Column(DateTime, default=func.now())


class Verification(Base):
    __tablename__ = "verification_codes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    code = Column(String, nullable=False)
    expired = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())

# class Schedule(Base):
#     __tablename__ = "schedules"
    
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     start_time = Column(DateTime, nullable=False)
#     end_time = Column(DateTime, nullable=False)
#     status = Column(String, default="active")
#     # duration_hours = Column(Integer, nullable=False)
#     # duration_minutes = Column(Integer, nullable=False)
#     created_at = Column(DateTime, default=datetime.now())

#     # # Связи
#     # teacher = relationship("Teacher", back_populates="schedules")
#     # student = relationship("Student", back_populates="schedules")

#     # Уникальное ограничение
#     __table_args__ = (UniqueConstraint("teacher_id", "student_id", "start_time", "end_time", name="_teacher_student_time_uc"),)

