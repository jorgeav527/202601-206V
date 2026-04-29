from flask import Blueprint, flash, redirect, render_template, request, url_for
 
from .db import get_db_connection, get_post
 
main = Blueprint("main", __name__)
 
 
@main.route("/", methods=["GET"])
def home():
    return render_template("index.html")
 
 
@main.route("/post", methods=["GET"])
def get_all_post():
    conn = get_db_connection()
    posts = conn.execute(
        "SELECT * FROM posts ORDER BY id DESC"
    ).fetchall()
    conn.close()
 
    return render_template("post/list.html", posts=posts)
 
 
@main.route("/post/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"].strip()
        content = request.form["content"].strip()
 
        if not title:
            flash("El título es obligatorio.", "danger")
        elif not content:
            flash("El contenido es obligatorio.", "danger")
        else:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO posts (title, content) VALUES (?, ?)",
                (title, content),
            )
            conn.commit()
            conn.close()
 
            flash("Post creado correctamente.", "success")
            return redirect(url_for("main.get_all_post"))
 
    return render_template("post/create.html")
 
 
@main.route("/post/<int:id>")
def get_post_detail(id):
    post = get_post(id)
    return render_template("post/single.html", post=post)
 
 
@main.route("/post/<int:id>/edit", methods=["GET", "POST"])
def edit(id):
    post = get_post(id)
 
    if request.method == "POST":
        title = request.form["title"].strip()
        content = request.form["content"].strip()
 
        if not title:
            flash("El título es obligatorio.", "danger")
        elif not content:
            flash("El contenido es obligatorio.", "danger")
        else:
            conn = get_db_connection()
            conn.execute(
                "UPDATE posts SET title = ?, content = ? WHERE id = ?",
                (title, content, id),
            )
            conn.commit()
            conn.close()
 
            flash("Post actualizado correctamente.", "success")
            return redirect(url_for("main.get_all_post"))
 
    return render_template("post/update.html", post=post)
 
 
@main.route("/post/<int:id>/delete", methods=["POST", "DELETE"])
def delete(id):
    get_post(id)
 
    conn = get_db_connection()
    conn.execute("DELETE FROM posts WHERE id = ?", (id,))
    conn.commit()
    conn.close()
 
    if request.method == "DELETE":
        return ""
 
    flash("Post eliminado correctamente.", "success")
    return redirect(url_for("main.get_all_post"))
 
 
@main.route("/checkhealth")
def check_health():
    return "<p>Todos los servicios están activos</p>"