from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Text, Table, UniqueConstraint, DateTime, Boolean, text, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import enum
import datetime

Base = declarative_base()

# class UserRole(enum.Enum):
#     TEACHER = "teacher"
#     STUDENT = "student"

# class User(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     username = Column(String, unique=True, nullable=False)
#     password_hash = Column(String, nullable=False)
#     email = Column(String, unique=True, nullable=False)
#     role = Column(Enum(UserRole), nullable=False)
#     created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))

#     # Связи
#     teacher = relationship("Teacher", back_populates="user", uselist=False)
#     student = relationship("Student", back_populates="user", uselist=False)
#     # messages_sent = relationship("Message", back_populates="sender", foreign_keys="Message.sender_id")
#     # messages_received = relationship("Message", back_populates="receiver", foreign_keys="Message.receiver_id")


class Teacher(Base):
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(36), nullable=False)
    surname = Column(String(36), nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))


class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(36), nullable=False)
    surname = Column(String(36), nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(36), nullable=False)
    surname = Column(String(36), nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())

    is_user = Column(Boolean, default=True, server_default=text('true'), nullable=False)
    is_student = Column(Boolean, default=False, server_default=text('false'), nullable=False)
    is_teacher = Column(Boolean, default=False, server_default=text('false'), nullable=False)
    is_admin = Column(Boolean, default=False, server_default=text('false'), nullable=False)
    is_super_admin = Column(Boolean, default=False, server_default=text('false'), nullable=False)

    # extend_existing = True


class Schedule(Base):
    __tablename__ = "schedules"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    status = Column(String, default="active")
    # duration_hours = Column(Integer, nullable=False)
    # duration_minutes = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))

    # # Связи
    # teacher = relationship("Teacher", back_populates="schedules")
    # student = relationship("Student", back_populates="schedules")

    # Уникальное ограничение
    __table_args__ = (UniqueConstraint("teacher_id", "student_id", "start_time", "end_time", name="_teacher_student_time_uc"),)

class Verification(Base):
    __tablename__ = "verification_codes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    code = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
