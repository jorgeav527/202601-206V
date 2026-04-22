import sqlite3

from flask import Flask, flash, redirect, render_template, request, url_for, abort

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("basedatos.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route("/post", methods=["GET"])
def get_all_post():
    conn = get_db_connection()
    posts = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()
    return render_template("post/list.html", posts=posts)


@app.route("/post/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title or not content:
            flash("Title is required!")
        else:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO posts (title, content) VALUES (?, ?)", (title, content)
            )
            conn.commit()
            conn.close()
            return redirect(url_for("get_all_post"))

    if request.method == "GET":
        return render_template("post/create.html")


@app.route("/post/<int:id>")
def get_post_detail(id):
    post = get_post(id)
    return render_template("post/single.html", post=post)


@app.route("/post/<int:id>/edit", methods=("GET", "POST"))
def edit(id):
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Title is required!")
        else:
            conn = get_db_connection()
            conn.execute(
                "UPDATE posts SET title = ?, content = ? WHERE id = ?",
                (title, content, id),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("get_all_post"))

    if request.method == "GET":
        return render_template("post/update.html", post=post)


@app.route("/post/<int:id>/delete", methods=("POST",))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute("DELETE FROM posts WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post["title"]))
    return redirect(url_for("get_all_post"))


@app.route("/checkheald")
def hello_world():
    return "<p>Todos los sevicion estan activos</p>"
