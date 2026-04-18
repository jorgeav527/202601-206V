from flask import Flask, request, render_template
import csv
import os

app = Flask(__name__)

@app.route("/count", methods=["GET", "POST"])
def count():
    if request.method == "GET":
        return render_template("index.html")

    # --- POST ---
    nombre = request.form["nombre"]
    edad = request.form["edad"]
    casado = "casado" in request.form

    archivo_csv = "personas.csv"
    archivo_existe = os.path.exists(archivo_csv)

    # Guardar persona
    with open(archivo_csv, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not archivo_existe:
            writer.writerow(["nombre", "edad", "casado"])
        writer.writerow([nombre, edad, casado])

    # Contar personas
    with open(archivo_csv, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        total = sum(1 for _ in reader) - 1  # quitar header

    return render_template(
        "response.html",
        personas_registradas=total
    )