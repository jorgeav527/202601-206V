# API REST de Estudiantes con FastAPI
 
Proyecto final de API REST para la gestión de estudiantes utilizando FastAPI y SQLite.
 
## Tecnologías utilizadas
 
- Python
- FastAPI
- SQLite
- SQLModel
- Jinja2
- JSON
 
## Modelo de datos
 
Cada estudiante tiene la siguiente estructura:
 
```json
{
  "id": 1,
  "dni": "12345678",
  "name": "Juan Pérez",
  "age": 20,
  "grade": 15.5,
  "is_approved": true,
  "created_at": "timestamp",
  "updated_at": "timestamp"
}