# 🎓 Student Management Portal

A simple **Student Management Portal** built using Python and Flask that allows management of students, teachers, attendance, assignments, marks, events, and announcements.

This project demonstrates a **basic ERP-style system for educational institutes** where students, teachers, and admins have different dashboards.

---

## 🚀 Features

### 👨‍🎓 Student

* View attendance
* View assignments
* Check internal marks
* View timetable
* View events
* View announcements

### 👩‍🏫 Teacher

* Mark student attendance
* Upload assignments
* Enter internal marks
* View timetable
* View announcements

### 👨‍💼 Admin

* Manage system data
* Add announcements
* Add events
* Update timetable
* Manage assignments and marks

---

## 🛠️ Tech Stack

Frontend:

* HTML
* CSS

Backend:

* Python
* Flask

Database:

* SQLite

Development Tools:

* Git
* Visual Studio Code

---

## 📂 Project Structure

```
student_management_portal
│
├── app.py
├── init_db.py
├── database.db
│
├── templates
│   ├── login.html
│   ├── login_student.html
│   ├── login_teacher.html
│   ├── login_admin.html
│   ├── dashboard_student.html
│   ├── dashboard_teacher.html
│   ├── dashboard_admin.html
│   ├── attendance.html
│   ├── assignments.html
│   ├── marks.html
│   ├── timetable.html
│   ├── events.html
│   └── announcements.html
│
└── static
    └── style.css
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/rutujakolate1703-bot/student-management-portal.git
```

Navigate into the folder:

```
cd student-management-portal
```

---

### 2️⃣ Install Dependencies

Make sure Python is installed.

Install Flask:

```
pip install flask
```

---

### 3️⃣ Create the Database

Run:

```
python init_db.py
```

This will create the database file.

---

### 4️⃣ Run the Application

Start the Flask server:

```
python app.py
```

Open the application in your browser:

```
http://127.0.0.1:5000
```

---

## 🔑 Default Login Credentials

Admin

```
Username: admin
Password: 123
```

Teacher

```
Username: teacher
Password: 123
```

Student

```
Username: student
Password: 123
```

---

## 📸 Screenshots

You can add screenshots of:

* Login page
* Student dashboard
* Teacher dashboard
* Admin dashboard

---

## 🔮 Future Improvements

* File upload for assignments
* QR-based attendance system
* Email notifications
* Role-based authentication
* Modern dashboard UI
* Deployment to cloud

---

## 🤝 Contributing

Contributions are welcome.
Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👩‍💻 Author

Developed as a learning project for understanding **Flask web development and database integration**.
