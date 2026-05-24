from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create database table
def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            roll TEXT,
            marks INTEGER
        )
    ''')

    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        name = request.form['name']
        roll = request.form['roll']
        marks = request.form['marks']

        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO students (name, roll, marks) VALUES (?, ?, ?)",
            (name, roll, marks)
        )

        conn.commit()
        conn.close()

    # Fetch all students
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)