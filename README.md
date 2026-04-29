# Proyecto Flask - Blog de Publicaciones
 
Este proyecto es una aplicación web básica desarrollada con Flask. Permite crear, listar, visualizar, actualizar y eliminar publicaciones usando una base de datos SQLite.
 
## Tecnologías utilizadas
 
- Python
- Flask
- SQLite
- Bootstrap 5
- HTMX
- Alpine.js
- HTML
- CSS
 
## Estructura del proyecto
 
```text
202601-206V/
│
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── routes.py
│
├── static/
│   └── main.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── navbar.html
│   └── post/
│       ├── create.html
│       ├── list.html
│       ├── single.html
│       └── update.html
│
├── basedatos.db
├── main.py
├── README.md
├── .gitignore
└── pyproject.toml