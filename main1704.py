from flask import Flask, request, render_template
import csv
import os

app = Flask(__name__)  # instancia de Flask

@app.route("/hello")  # ruta / endpoint
def hello_world():
    return "<p>Hello, Cristobal!</p>"

@app.route("/ch")  # ruta / endpoint
def ch():
    return "Ok"

#Con Control + C detengo el servidor
#Poniendo esto revive el servidor: uv run python -m flask --app main1704 run
#si cambio algo, debo detener el servidor y volver a revivirlo, pero siempre al inicio debo guardar el file

@app.route("/readme") #lo voy a enviar al cliente
def r_w():
    with open("README.md") as file:
        content = file.read()
    return content

#@app.route("/count") #mientras actualice la pagina, se va actualizando el archivo count cuando empiece a actualizar la pagina web
#def count():
 #   with open("count.txt", mode="r") as file:
  #      count = int(file.read())
   # count +=1
    #with open ("count.txt", mode="w") as file:
    #   file.write(str(count))
    #return f'Numero de visitas: {count}'

@app.route("/count", methods=["GET", "POST"]) 
#debo poner arriba request al inicio en la linea del import flask
#
def count():
    if request.method == "GET": #me vas a retornar un string, 
        return render_template("index.html")
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = request.form["edad"]
        casado = request.form["casado"]
        
        archivo_csv="registros.csv"

        print(nombre, edad, casado)
        with open("count.csv", mode="r") as file:
            count = int(file.read())
        count += 1
        with open("count.csv", mode="w") as file:
            file.write(str(count))
        return render_template("response.html", count_response=count)


@app.route("/count", methods=["GET", "POST"])
def count():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = request.form["edad"]
        casado = request.form["casado"]

        archivo_csv = "registros.csv"

        # Verifica si el archivo CSV ya existe
        existe_archivo = os.path.exists(archivo_csv)

        # Guardamos el nuevo registro en el CSV
        with open(archivo_csv, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Si el archivo no existe, agregamos encabezados
            if not existe_archivo:
                writer.writerow(["nombre", "edad", "casado"])

            writer.writerow([nombre, edad, casado])

        # Leemos todos los registros del CSV
        registros = []

        with open(archivo_csv, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                registros.append(row)

        count = len(registros)

        return render_template(
            "response.html",
            count_response=count,
            registros=registros
        )

