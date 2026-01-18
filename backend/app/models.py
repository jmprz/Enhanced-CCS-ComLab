from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from . import models, schemas
from .database import engine, get_db
from . database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, unique=True, index=True) # e.g., 2021-0001
    full_name = Column(String)
    role = Column(String)  # Admin, Teacher, Student
    password_hash = Column(String)

class Computer(Base):
    __tablename__ = "computers"
    id = Column(Integer, primary_key=True, index=True)
    pc_name = Column(String, unique=True) # e.g., LAB1-PC01
    status = Column(String, default="offline") # online, offline, idle

class ActivityLog(Base):
    __tablename__ = "activity_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    computer_id = Column(Integer, ForeignKey("computers.id"))
    activity_type = Column(String) # login, logout, idle
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    computer_id = Column(Integer, ForeignKey("computers.id"))
    alert_type = Column(String) # violation, idle_warning
    message = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)