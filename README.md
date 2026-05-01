# Proyecto Flask - Registro de Usuarios

Aplicación básica desarrollada con Flask para registrar usuarios y guardar sus datos en un archivo CSV.

## Funcionalidades

- Registro de usuarios mediante formulario.
- Almacenamiento de nombre, edad y estado civil.
- Uso de archivo `usuarios.csv`.
- Conteo total de usuarios registrados.
- Interfaz mejorada con Bootstrap.
- Código organizado en carpetas.

## Estructura del proyecto

```text
202601-206V/
├── main.py
├── routes/
│   └── users.py
├── services/
│   └── csv_service.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── response.html
├── static/
│   └── css/
│       └── styles.css
├── usuarios.csv
├── README.md
└── .gitignore
```

## Requisitos

- Python 3
- Flask

## Instalación y ejecución

Clonar el repositorio:

```bash
git clone https://github.com/jorgeav527/202601-206V.git
```

Entrar al proyecto:

```bash
cd 202601-206V
```

Cambiar a la rama de trabajo:

```bash
git checkout brach-maria
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual en Windows:

```bash
venv\Scripts\activate
```

Instalar Flask:

```bash
pip install flask
```

Ejecutar la aplicación:

```bash
python main.py
```

Abrir en el navegador:

```text
http://127.0.0.1:5000
```

## Rutas disponibles

| Ruta | Descripción |
|---|---|
| `/` | Redirige al formulario |
| `/count` | Muestra y procesa el formulario |
| `/hello` | Ruta de prueba |
| `/ch` | Ruta de verificación |
| `/readme` | Muestra el contenido del README |

## Autor

María Antuanet Michca Maguiña