from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy import func
from sqlalchemy.orm import Session

from ProyectoFinal.database import SessionLocal
from ProyectoFinal.models import Student
from ProyectoFinal.schemas import StudentCreate, StudentResponse, StudentUpdate

router = APIRouter()

templates = Jinja2Templates(directory="ProyectoFinal/templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    existing = db.query(Student).filter(Student.dni == student.dni).first()

    if existing:
        raise HTTPException(status_code=400, detail="El DNI ya existe")

    new_student = Student(**student.model_dump())

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@router.get("/students", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


@router.post("/students/bulk", response_model=list[StudentResponse], status_code=201)
def bulk_create_students(students: list[StudentCreate], db: Session = Depends(get_db)):
    new_students = []

    for student in students:
        existing = db.query(Student).filter(Student.dni == student.dni).first()

        if existing:
            raise HTTPException(
                status_code=400,
                detail=f"El DNI {student.dni} ya existe"
            )

        new_students.append(Student(**student.model_dump()))

    db.add_all(new_students)
    db.commit()

    for student in new_students:
        db.refresh(student)

    return new_students


@router.get("/students/average")
def get_average_grade(db: Session = Depends(get_db)):
    average = db.query(func.avg(Student.grade)).scalar()

    return {
        "average_grade": round(average, 2) if average is not None else 0
    }


@router.get("/students/table")
def students_table(request: Request, db: Session = Depends(get_db)):
    students = db.query(Student).all()

    return templates.TemplateResponse(
        request=request,
        name="partials/students_table.html",
        context={"students": students}
    )


@router.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    return student


@router.patch("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    data = student_data.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(student, key, value)

    student.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(student)

    return student


@router.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    db.delete(student)
    db.commit()

    return {"message": "Estudiante eliminado correctamente"}