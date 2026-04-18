from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ch")
def check_held():
    return "OK"

@app.route("/readme")
def r_w():
    with open("README.md") as file:
        content = file.read()
    return content

@app.route("/count")
def count():

    with open("count.txt", mode="r") as file:
        count = int(file.read())
    
    count += 1
    with open("count.txt", mode="w") as file:
        file.write(str(count))
        
    return f'Numero de visitas: {count}'