from flask import Flask, request

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
        forma = """
        <form action="/count" method="post">
            <button type="submit">Incrementar</button>
        </form>
        """
        return forma
    if request.method == "POST":
        with open("count.txt", mode="r") as file:
            count = int(file.read())
        count += 1
        with open("count.txt", mode="w") as file:
            file.write(str(count))
        return f'Numero de visitas: {count}'