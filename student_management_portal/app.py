from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login_student")
def login_student():
    return render_template("login_student.html")


@app.route("/login_teacher")
def login_teacher():
    return render_template("login_teacher.html")


@app.route("/login_admin")
def login_admin():
    return render_template("login_admin.html")


@app.route("/login", methods=["POST"])
def do_login():
    username = request.form["username"]
    password = request.form["password"]

    conn = db()
    user = conn.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    ).fetchone()

    if user:
        role = user["role"]

        if role == "student":
            return redirect("/student")

        if role == "teacher":
            return redirect("/teacher")

        if role == "admin":
            return redirect("/admin")

    return "Invalid login"


@app.route("/student")
def student_dashboard():
    return render_template("dashboard_student.html")


@app.route("/teacher")
def teacher_dashboard():
    return render_template("dashboard_teacher.html")


@app.route("/admin")
def admin_dashboard():
    return render_template("dashboard_admin.html")


@app.route("/attendance")
def attendance():
    conn = db()
    data = conn.execute("SELECT * FROM attendance").fetchall()
    return render_template("attendance.html", data=data)


@app.route("/assignments")
def assignments():
    conn = db()
    data = conn.execute("SELECT * FROM assignments").fetchall()
    return render_template("assignments.html", data=data)


@app.route("/marks")
def marks():
    conn = db()
    data = conn.execute("SELECT * FROM marks").fetchall()
    return render_template("marks.html", data=data)


@app.route("/timetable")
def timetable():
    conn = db()
    data = conn.execute("SELECT * FROM timetable").fetchall()
    return render_template("timetable.html", data=data)


@app.route("/events")
def events():
    conn = db()
    data = conn.execute("SELECT * FROM events").fetchall()
    return render_template("events.html", data=data)


@app.route("/announcements")
def announcements():
    conn = db()
    data = conn.execute("SELECT * FROM announcements").fetchall()
    return render_template("announcements.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)