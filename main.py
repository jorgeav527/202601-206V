from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('basedatos.db')
    # conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/checkheald")
def hello_world():
    return "<p>Todos los sevicion estan activos</p>"
