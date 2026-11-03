from flask import Flask, render_template, request, redirect, session
import psycopg2

app = Flask(__name__)
app.secret_key = "12345"

# PostgreSQL Database Connection
con = psycopg2.connect(
    host="localhost",
    database="student_assign",
    user="postgres",
    password="root",
    port="5432"
)

# Create Tables
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS assignments (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    subject VARCHAR(100)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS submissions (
    id SERIAL PRIMARY KEY,
    student_name VARCHAR(100),
    assignment_title VARCHAR(100),
    answer TEXT
)
""")

con.commit()
cur.close()
con.close()


# Registration
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        db = psycopg2.connect(
            host="localhost",
            database="student_assign",
            user="postgres",
            password="root"
        )

        cur = db.cursor()

        cur.execute(
            "INSERT INTO users(name,email,password) VALUES(%s,%s,%s)",
            (name, email, password)
        )

        db.commit()
        cur.close()
        db.close()

        return redirect('/login')

    return render_template('register.html')

# Home Page (Front Page)
@app.route('/')
def home():
    return render_template('index.html')


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        db = psycopg2.connect(
            host="localhost",
            database="student_assign",
            user="postgres",
            password="root"
        )

        cur = db.cursor()

        cur.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )

        user = cur.fetchone()

        cur.close()
        db.close()

        if user:
            session['name'] = user[1]
            return redirect('/dashboard')

        return "Invalid Email or Password"

    return render_template('login.html')


# Dashboard
@app.route('/dashboard')
def dashboard():

    if 'name' not in session:
        return redirect('/login')

    db = psycopg2.connect(
        host="localhost",
        database="student_assign",
        user="postgres",
        password="root"
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM assignments")

    assignments = cur.fetchall()

    cur.close()
    db.close()

    return render_template(
        'dashboard.html',
        assignments=assignments,
        name=session['name']
    )

@app.route('/add_assignment', methods=['GET', 'POST'])
def add_assignment():

    if request.method == 'POST':

        title = request.form['title']
        subject = request.form['subject']

        db = psycopg2.connect(
            host="localhost",
            database="student_db",
            user="postgres",
            password="your_password"
        )

        cur = db.cursor()

        cur.execute(
            "INSERT INTO assignments(title, subject) VALUES(%s,%s)",
            (title, subject)
        )

        db.commit()
        cur.close()
        db.close()

        return redirect('/dashboard')

    return render_template('add_assignment.html')

# Assignment Submission
@app.route('/submit', methods=['GET', 'POST'])
def submit():

    if 'name' not in session:
        return redirect('/login')

    if request.method == 'POST':

        title = request.form['title']
        answer = request.form['answer']

        db = psycopg2.connect(
            host="localhost",
            database="student_assign",
            user="postgres",
            password="root"
        )

        cur = db.cursor()

        cur.execute("""
            INSERT INTO submissions
            (student_name, assignment_title, answer)
            VALUES (%s, %s, %s)
        """, (session['name'], title, answer))

        db.commit()
        cur.close()
        db.close()

        return redirect('/dashboard')

    return render_template('submit.html')


# Logout
@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)