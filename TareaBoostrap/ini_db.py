import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "basedatos.db"
SCHEMA = BASE_DIR / "schema.sql"


def init_db():
    connection = sqlite3.connect(DATABASE)

    with open(SCHEMA, "r", encoding="utf-8") as f:
        connection.executescript(f.read())

    cur = connection.cursor()
    cur.execute(
        "INSERT INTO posts (title, content) VALUES (?, ?)",
        ("First Post", "Content for the first post"),
    )

    connection.commit()
    connection.close()


if __name__ == "__main__":
    init_db()
    print("Database initialized.")