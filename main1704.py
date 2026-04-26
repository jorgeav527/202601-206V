from flask import Flask

app = Flask(__name__)  # instancia de Flask

@app.route("/hello")  # ruta / endpoint
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ch")  # ruta / endpoint
def ch():
    return "Ok"

#Con Control + C detengo el servidor
#Poniendo esto revive el servidor: uv run python -m flask --app main1704 run

