import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

DATABASE = os.getenv("DATABASE", "basedatos.db")


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn