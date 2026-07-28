import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Students Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    department TEXT
)
""")

# Marks Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS marks(
    mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject TEXT,
    mark INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
)
""")

conn.commit()

def add_student():
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")

    cursor.execute(
        "INSERT INTO students(name, age, department) VALUES(?, ?, ?)",
        (name, age, department)
    )

    conn.commit()
    print("Student Added Successfully!")

def add_marks():
    student_id = int(input("Enter Student ID: "))
    subject = input("Enter Subject: ")
    mark = int(input("Enter Mark: "))

    cursor.execute(
        "INSERT INTO marks(student_id, subject, mark) VALUES(?, ?, ?)",
        (student_id, subject, mark)
    )

    conn.commit()
    print("Mark Added Successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    print("\nSTUDENT DETAILS")
    for row in data:
        print(row)

def view_marks():
    cursor.execute("""
    SELECT students.name,
           marks.subject,
           marks.mark
    FROM marks
    JOIN students
    ON marks.student_id = students.student_id
    """)

    data = cursor.fetchall()

    print("\nMARK DETAILS")
    for row in data:
        print(row)

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Add Marks")
    print("3. View Students")
    print("4. View Marks")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        add_marks()

    elif choice == "3":
        view_students()

    elif choice == "4":
        view_marks()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")

conn.close()