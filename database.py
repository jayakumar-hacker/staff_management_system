import sqlite3

conn=sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE if not exists staff(
id Integer PRIMARY KEY AUTOINCREMENT,
name text not null,
email text unique,
role text,
salary real check(salary>=0),
department text,
created_at timestamp default current_timestamp)
""")


cursor.execute("""
CREATE TABLE if NOT EXISTS admin(
id Integer PRIMARY KEY AUTOINCREMENT,
USERNAME TEXT UNIQUE,
role text not null,
password text not null)
""")

conn.commit()
conn.close()
