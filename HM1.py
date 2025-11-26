import sqlite3

connection = sqlite3.connect("AnimalKingdom.sl3")
cur = connection.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Animals (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT
);
""")
cur.execute("DELETE FROM Animals;")
animals = [
    ("Лев", "Ссавець"),
    ("Крокодил", "Плазун"),
    ("Орел", "Птах"),
    ("Хамелеон", "Плазун"),
    ("Мавпа", "Ссавець")
]
cur.executemany("INSERT INTO Animals (name, type) VALUES (?, ?);", animals)
cur.execute("UPDATE Animals SET name='Сокіл' WHERE name='Орел';")
print("Ссавці:")
cur.execute("SELECT * FROM Animals WHERE type='Ссавець';")
print(cur.fetchall())
print("\nУсі звірі:")
cur.execute("SELECT * FROM Animals;")
print(cur.fetchall())
connection.commit()
connection.close()
"""Завдання 1"""