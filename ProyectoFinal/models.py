from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String

from ProyectoFinal.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(Float, nullable=False)
    is_approved = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)