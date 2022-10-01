import _sqlite3

con = _sqlite3.connect('to_do_list._sqlite')
cur = con.cursor()

def check_bd():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS takes(
    id INT PRIMARY KEY,
    user INT,
    title VARCHAR(255) NOT NULL,
    discriptions VARCHAR(255),
    deadleline_date DATETIME,
    FORGEIGN KEY (user_id) REFERENCES user(id)
    );
    """)

    con.commit()

def add_user(username, password, name):
    cur.execute("""
    INSERT INTO users (username, password, name)
    VALUES (?, ?, ?)""",(username, password, name))
    con.commit()