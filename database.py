import sqlite3

DB_NAME = "data.db"
def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn=get_connection()    
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


def add_staff(name,email,salary,role,department):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO STAFF (name,email,salary,role,department) values
    (?,?,?,?,?)
    """,(name,email,salary,role,department))
    conn.commit()
    conn.close()

def get_all_staff():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM STAFF")
    data = cursor.fetchall()
    return data
    conn.commit()
    conn.close()

def get_staff_by_id(staff_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("select * from staff where id = ?",(staff_id,))
    data = cursor.fetchone()
    return data
    conn.commit()
    conn.close()

def update_staff(staff_id,name,email,salary,role,department):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE staff
    set name=?, email=?, salary=?,role=?,department=?
    where id=?
    """,(name,email,salary,role,department,staff_id))
    conn.commit()
    conn.close()


def delete_staff(staff_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE from staff where id=?",(staff_id,))
    conn.commit()
    conn.close()

def create_admin(username,password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTo admin (username,password,role) values (?,?,?)
    """,(username,password,"admin"))
    conn.commit()
    conn.close()
    
def verify_admin(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT password from admin where username=?""",(username,))

    result = cursor.fetchone()
    conn.close()
    return result[0]
