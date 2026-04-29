import sqlite3
 
DATABASE_NAME = "students.db"
 
 
def get_connection():

    conn = sqlite3.connect(DATABASE_NAME)

    conn.row_factory = sqlite3.Row

    return conn
 
 
def create_table():

    conn = get_connection()
 
    conn.execute(

        """

        CREATE TABLE IF NOT EXISTS students (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            dni TEXT NOT NULL UNIQUE,

            name TEXT NOT NULL,

            age INTEGER NOT NULL,

            grade REAL NOT NULL,

            is_approved INTEGER NOT NULL,

            created_at TEXT NOT NULL,

            updated_at TEXT NOT NULL

        )

        """

    )
 
    conn.commit()

    conn.close()
 