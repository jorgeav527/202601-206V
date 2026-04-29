from datetime import datetime

from typing import Optional
 
from pydantic import BaseModel, Field, field_validator
 
 
class StudentCreate(BaseModel):

    dni: str = Field(..., min_length=8, max_length=8)

    name: str = Field(..., min_length=2, max_length=100)

    age: int = Field(..., gt=0, le=120)

    grade: float = Field(..., ge=0, le=20)

    is_approved: bool
 
    @field_validator("dni")

    @classmethod

    def validate_dni(cls, value):

        if not value.isdigit():

            raise ValueError("El DNI debe contener solo números.")

        return value
 
    @field_validator("name")

    @classmethod

    def validate_name(cls, value):

        value = value.strip()

        if not value:

            raise ValueError("El nombre no puede estar vacío.")

        return value
 
 
class StudentUpdate(BaseModel):

    dni: Optional[str] = Field(default=None, min_length=8, max_length=8)

    name: Optional[str] = Field(default=None, min_length=2, max_length=100)

    age: Optional[int] = Field(default=None, gt=0, le=120)

    grade: Optional[float] = Field(default=None, ge=0, le=20)

    is_approved: Optional[bool] = None
 
    @field_validator("dni")

    @classmethod

    def validate_dni(cls, value):

        if value is not None and not value.isdigit():

            raise ValueError("El DNI debe contener solo números.")

        return value
 
    @field_validator("name")

    @classmethod

    def validate_name(cls, value):

        if value is not None:

            value = value.strip()

            if not value:

                raise ValueError("El nombre no puede estar vacío.")

        return value
 
 
class StudentResponse(BaseModel):

    id: int

    dni: str

    name: str

    age: int

    grade: float

    is_approved: bool

    created_at: datetime

    updated_at: datetime
 
 
class AverageResponse(BaseModel):

    average_grade: float

    total_students: int
 