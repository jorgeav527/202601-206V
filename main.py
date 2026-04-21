from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("count"))

@app.route("/hello")
def hello_world():
    return "<p>Hello, Alarcon!</p>"

@app.route("/ch")
def check_held():
    return "OK"

@app.route("/readme")
def r_w():
    with open("README.md", encoding="utf-8") as file:
        content = file.read()
    return content

@app.route("/count", methods=["GET", "POST"])
def count():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = request.form["edad"]
        casado = "Sí" if "casado" in request.form else "No"

        # Guardar usuario en CSV
        with open("usuarios.csv", mode="a", encoding="utf-8") as file:
            file.write(f"{nombre},{edad},{casado}\n")

        # Leer todos los usuarios
        with open("usuarios.csv", mode="r", encoding="utf-8") as file:
            usuarios = file.readlines()

        count = len(usuarios)

        return render_template("response.html", count_response=count)

if __name__ == "__main__":
    app.run(debug=True)