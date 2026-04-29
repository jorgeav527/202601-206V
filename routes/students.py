from datetime import datetime

from typing import List
 
from fastapi import APIRouter, HTTPException, Request, status

from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
 
from database.connection import get_connection

from models.student import (

    AverageResponse,

    StudentCreate,

    StudentResponse,

    StudentUpdate,

)
 
router = APIRouter(

    prefix="/students",

    tags=["Students"]

)
 
templates = Jinja2Templates(directory="templates")
 
 
def row_to_student(row):

    return {

        "id": row["id"],

        "dni": row["dni"],

        "name": row["name"],

        "age": row["age"],

        "grade": row["grade"],

        "is_approved": bool(row["is_approved"]),

        "created_at": row["created_at"],

        "updated_at": row["updated_at"],

    }
 
 
@router.post(

    "",

    response_model=StudentResponse,

    status_code=status.HTTP_201_CREATED

)

def create_student(student: StudentCreate):

    conn = get_connection()
 
    existing_student = conn.execute(

        "SELECT * FROM students WHERE dni = ?",

        (student.dni,)

    ).fetchone()
 
    if existing_student:

        conn.close()

        raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,

            detail="Ya existe un estudiante con ese DNI."

        )
 
    now = datetime.utcnow().isoformat()
 
    cursor = conn.execute(

        """

        INSERT INTO students (

            dni, name, age, grade, is_approved, created_at, updated_at

        )

        VALUES (?, ?, ?, ?, ?, ?, ?)

        """,

        (

            student.dni,

            student.name,

            student.age,

            student.grade,

            int(student.is_approved),

            now,

            now,

        )

    )
 
    conn.commit()
 
    new_student = conn.execute(

        "SELECT * FROM students WHERE id = ?",

        (cursor.lastrowid,)

    ).fetchone()
 
    conn.close()
 
    return row_to_student(new_student)
 
 
@router.get(

    "",

    response_model=List[StudentResponse]

)

def get_students():

    conn = get_connection()
 
    students = conn.execute(

        "SELECT * FROM students ORDER BY id ASC"

    ).fetchall()
 
    conn.close()
 
    return [row_to_student(student) for student in students]
 
 
@router.get(

    "/average",

    response_model=AverageResponse

)

def get_average_grade():

    conn = get_connection()
 
    result = conn.execute(

        """

        SELECT

            COUNT(*) AS total_students,

            AVG(grade) AS average_grade

        FROM students

        """

    ).fetchone()
 
    conn.close()
 
    total_students = result["total_students"]
 
    if total_students == 0:

        return {

            "average_grade": 0,

            "total_students": 0

        }
 
    return {

        "average_grade": round(result["average_grade"], 2),

        "total_students": total_students

    }
 
 
@router.get(

    "/table",

    response_class=HTMLResponse

)

def get_students_table(request: Request):

    conn = get_connection()
 
    students = conn.execute(

        "SELECT * FROM students ORDER BY id ASC"

    ).fetchall()
 
    conn.close()
 
    students_list = [row_to_student(student) for student in students]
 
    return templates.TemplateResponse(

        request=request,

        name="partials/students_table.html",

        context={

            "students": students_list

        }

    )
 
 
@router.get(

    "/{student_id}",

    response_model=StudentResponse

)

def get_student_by_id(student_id: int):

    conn = get_connection()
 
    student = conn.execute(

        "SELECT * FROM students WHERE id = ?",

        (student_id,)

    ).fetchone()
 
    conn.close()
 
    if student is None:

        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,

            detail="Estudiante no encontrado."

        )
 
    return row_to_student(student)
 
 
@router.put(

    "/{student_id}",

    response_model=StudentResponse

)

def update_student(student_id: int, student_data: StudentUpdate):

    conn = get_connection()
 
    student = conn.execute(

        "SELECT * FROM students WHERE id = ?",

        (student_id,)

    ).fetchone()
 
    if student is None:

        conn.close()

        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,

            detail="Estudiante no encontrado."

        )
 
    update_data = student_data.model_dump(exclude_unset=True)
 
    if not update_data:

        conn.close()

        raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,

            detail="Debe enviar al menos un campo para actualizar."

        )
 
    if "dni" in update_data:

        existing_student = conn.execute(

            "SELECT * FROM students WHERE dni = ? AND id != ?",

            (update_data["dni"], student_id)

        ).fetchone()
 
        if existing_student:

            conn.close()

            raise HTTPException(

                status_code=status.HTTP_400_BAD_REQUEST,

                detail="Ya existe otro estudiante con ese DNI."

            )
 
    fields = []

    values = []
 
    for key, value in update_data.items():

        if key == "is_approved":

            value = int(value)
 
        fields.append(f"{key} = ?")

        values.append(value)
 
    updated_at = datetime.utcnow().isoformat()

    fields.append("updated_at = ?")

    values.append(updated_at)
 
    values.append(student_id)
 
    query = f"""

        UPDATE students

        SET {", ".join(fields)}

        WHERE id = ?

    """
 
    conn.execute(query, values)

    conn.commit()
 
    updated_student = conn.execute(

        "SELECT * FROM students WHERE id = ?",

        (student_id,)

    ).fetchone()
 
    conn.close()
 
    return row_to_student(updated_student)
 
 
@router.delete(

    "/{student_id}",

    status_code=status.HTTP_200_OK

)

def delete_student(student_id: int):

    conn = get_connection()
 
    student = conn.execute(

        "SELECT * FROM students WHERE id = ?",

        (student_id,)

    ).fetchone()
 
    if student is None:

        conn.close()

        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,

            detail="Estudiante no encontrado."

        )
 
    conn.execute(

        "DELETE FROM students WHERE id = ?",

        (student_id,)

    )
 
    conn.commit()

    conn.close()
 
    return {

        "message": "Estudiante eliminado correctamente."

    }
 
 
@router.post(

    "/bulk",

    response_model=List[StudentResponse],

    status_code=status.HTTP_201_CREATED

)

def bulk_insert_students(students: List[StudentCreate]):

    conn = get_connection()
 
    created_students = []
 
    try:

        for student in students:

            existing_student = conn.execute(

                "SELECT * FROM students WHERE dni = ?",

                (student.dni,)

            ).fetchone()
 
            if existing_student:

                raise HTTPException(

                    status_code=status.HTTP_400_BAD_REQUEST,

                    detail=f"Ya existe un estudiante con el DNI {student.dni}."

                )
 
            now = datetime.utcnow().isoformat()
 
            cursor = conn.execute(

                """

                INSERT INTO students (

                    dni, name, age, grade, is_approved, created_at, updated_at

                )

                VALUES (?, ?, ?, ?, ?, ?, ?)

                """,

                (

                    student.dni,

                    student.name,

                    student.age,

                    student.grade,

                    int(student.is_approved),

                    now,

                    now,

                )

            )
 
            new_student = conn.execute(

                "SELECT * FROM students WHERE id = ?",

                (cursor.lastrowid,)

            ).fetchone()
 
            created_students.append(row_to_student(new_student))
 
        conn.commit()
 
    except HTTPException:

        conn.rollback()

        conn.close()

        raise
 
    conn.close()
 
    return created_students
 