from fastapi import FastAPI
from ProyectoFinal.database import Base, engine
from ProyectoFinal.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Examen API REST de Estudiantes",
    description="API para gestionar estudiantes - Proyecto Final - Cristobal Contreras",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "API REST de Estudiantes funcionando"}