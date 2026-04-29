from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__, template_folder="templatess")

ARCHIVO_CSV = "count.csv"


@app.route("/")
def inicio():
    return "Servidor funcionando. Entra a /count"


@app.route("/count", methods=["GET", "POST"])
def count():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = request.form["edad"]
        casado = request.form["casado"]

        existe_archivo = os.path.exists(ARCHIVO_CSV)

        with open(ARCHIVO_CSV, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if not existe_archivo:
                writer.writerow(["nombre", "edad", "casado"])

            writer.writerow([nombre, edad, casado])

        registros = []

        with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                registros.append(row)

        cantidad_registros = len(registros)

        return render_template(
            "response.html",
            count_response=cantidad_registros,
            registros=registros
        )

