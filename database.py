import sqlite3

class StudentDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('students.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                course TEXT
            )
        ''')
        self.conn.commit()

    def view_students(self):
        self.cursor.execute('SELECT * FROM students')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        )
