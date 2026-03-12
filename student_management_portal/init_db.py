import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
username TEXT,
password TEXT,
role TEXT
)
""")

cur.execute("""
CREATE TABLE attendance(
id INTEGER PRIMARY KEY AUTOINCREMENT,
student TEXT,
date TEXT,
status TEXT
)
""")

cur.execute("""
CREATE TABLE assignments(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
description TEXT,
due_date TEXT
)
""")

cur.execute("""
CREATE TABLE marks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
student TEXT,
subject TEXT,
marks INTEGER
)
""")

cur.execute("""
CREATE TABLE timetable(
id INTEGER PRIMARY KEY AUTOINCREMENT,
day TEXT,
subject TEXT,
time TEXT
)
""")

cur.execute("""
CREATE TABLE events(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
date TEXT,
description TEXT
)
""")

cur.execute("""
CREATE TABLE announcements(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
message TEXT
)
""")

cur.execute("INSERT INTO users (name,username,password,role) VALUES ('Admin','admin','123','admin')")
cur.execute("INSERT INTO users (name,username,password,role) VALUES ('Teacher','teacher','123','teacher')")
cur.execute("INSERT INTO users (name,username,password,role) VALUES ('Student','student','123','student')")

conn.commit()
conn.close()

print("Database created")