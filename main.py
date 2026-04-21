from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, Alarcon!</p>"

@app.route("/ch")
def check_held():
    return "OK"

@app.route("/readme")
def r_w():
    with open("README.md") as file:
        content = file.read()
    return content


@app.route("/count", methods=["GET", "POST"])
def count():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = request.form["edad"]
        casado = request.form["casado"]
        print(nombre, edad, casado)
        with open("count.txt", mode="r") as file:
            count = int(file.read())
        count += 1
        with open("count.txt", mode="w") as file:
            file.write(str(count))
        return render_template("response.html", count_response=count)