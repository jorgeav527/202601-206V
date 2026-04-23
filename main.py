import sqlite3
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("basedatos.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    conn.close()
    if post is None:
        # Retorna un error 404 en formato JSON
        abort(404, description="Post no encontrado")
    return post

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Bienvenido a la API de Posts", "status": "ok"})

@app.route("/post", methods=["GET"])
def get_all_post():
    conn = get_db_connection()
    posts_raw = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()
    posts = [dict(row) for row in posts_raw]
    return jsonify(posts)

@app.route("/post", methods=["POST"]) # Simplificado el path
def create():
    # Obtenemos datos de JSON en lugar de request.form
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return jsonify({"error": "Title and content are required!"}), 400
    
    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO posts (title, content) VALUES (?, ?)", (title, content)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    
    return jsonify({"id": new_id, "title": title, "content": content}), 200

@app.route("/post/<int:id>", methods=["GET"])
def get_post_detail(id):
    post = get_post(id)
    return jsonify(dict(post))

@app.route("/post/<int:id>", methods=["PUT"])
def edit(id):
    get_post(id)
    data = request.get_json()
    
    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return jsonify({"error": "Title is required!"}), 400

    conn = get_db_connection()
    conn.execute(
        "UPDATE posts SET title = ?, content = ? WHERE id = ?",
        (title, content, id),
    )
    conn.commit()
    conn.close()
    
    return jsonify({"id": id, "title": title, "content": content})

@app.route("/post/<int:id>", methods=["DELETE"])
def delete(id):
    get_post(id) # Verifica si existe antes de borrar
    conn = get_db_connection()
    conn.execute("DELETE FROM posts WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    
    # 204 No Content es el estándar para borrados exitosos sin retorno de data
    return '', 204

@app.route("/checkhealth") # Corregido typo 'checkheald'
def hello_world():
    return jsonify({
        "status": "active",
        "services": "all systems go"
    })

if __name__ == "__main__":
    app.run(debug=True)