from flask import Blueprint, request, render_template, redirect, url_for
from services.csv_service import save_user, count_users

users_bp = Blueprint("users", __name__)

@users_bp.route("/")
def home():
    return redirect(url_for("users.count"))

@users_bp.route("/hello")
def hello_world():
    return "<p>Hello, Alarcon!</p>"

@users_bp.route("/ch")
def check_held():
    return "OK"

@users_bp.route("/readme")
def r_w():
    with open("README.md", encoding="utf-8") as file:
        content = file.read()
    return content

@users_bp.route("/count", methods=["GET", "POST"])
def count():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = request.form["edad"]
        casado = "Sí" if "casado" in request.form else "No"

        save_user(nombre, edad, casado)
        total_users = count_users()

        return render_template("response.html", count_response=total_users)