#Proyecto Final - Cristobal Contreras

#1. Se creo una carpeta "ProyectoFinal" ubicado en la rama branch-cristobal
#2. Se utilizo uv para gestionar el entorno del proyecto
#3. Se usaron las librerias fastapi, uvicorn, sqlalchemy y jinja2
#4. Se creo una base de datos database.py
#5. Se creo el archivo models.py que incluye todos los campos solicitados por estudiante: id, DNI, nombre, años, nota, si esta aprobado, cuando fue creado el registro y cuando se actualizo.
#6. En schemas.py se definieron el tipo de registro que tendria cada campo del estudiante para la creación de los estudiantes
#7. En routes.py se definieron los endpoints
#8. En la subcarpeta templates, se creo un archivo students_table.html que incluye la estructura de la tabla de los estudiantes registrados
#9. Se creo main.py para el lanzamiento de la API y el uso de todas las rutas incluidas en el proyecto

#Para ejecutar
#1. Abrir la terminal - bash 
#2. Cambiar de rama: git checkout branch-cristobal
#3. Instalar dependencias: uv sync
#4. En el terminal, ingresar lo siguiente: uv run uvicorn ProyectoFinal.main:app --reload
#5. Abrir en el navegador los siguientes enlaces:
    #Enlace 1: http://127.0.0.1:8000/docs
    #Enlace 2: http://127.0.0.1:8000/students/table


