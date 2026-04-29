from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class StudentBase(BaseModel):
    dni: str
    name: str
    age: int
    grade: float
    is_approved: bool


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    dni: Optional[str] = None
    name: Optional[str] = None
    age: Optional[int] = None
    grade: Optional[float] = None
    is_approved: Optional[bool] = None


class StudentResponse(StudentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True