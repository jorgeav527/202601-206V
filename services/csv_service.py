CSV_FILE = "usuarios.csv"

def save_user(nombre, edad, casado):
    with open(CSV_FILE, mode="a", encoding="utf-8") as file:
        file.write(f"{nombre},{edad},{casado}\n")

def count_users():
    try:
        with open(CSV_FILE, mode="r", encoding="utf-8") as file:
            users = file.readlines()
        return len(users)
    except FileNotFoundError:
        return 0