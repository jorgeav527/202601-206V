from fastapi import FastAPI, Request

from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
 
from database.connection import create_table

from routes.students import router as students_router
 
app = FastAPI(

    title="API REST de Estudiantes",

    description="Proyecto final desarrollado con FastAPI y SQLite3",

    version="1.0.0"

)
 
templates = Jinja2Templates(directory="templates")
 
 
@app.on_event("startup")

def startup():

    create_table()
 
 
@app.get("/", response_class=HTMLResponse)

def home(request: Request):

    return templates.TemplateResponse(

        request=request,

        name="index.html",

        context={}

    )
 
 
app.include_router(students_router)
 