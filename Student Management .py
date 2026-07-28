import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
student_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
class_name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers(
teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
subject TEXT
)
""")

conn.commit()