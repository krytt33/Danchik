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

def login(username, password) -> bool:
    result = cur.execute("""
        SELECT username, password, name
        FROM users
        WHERE username = (?)""",(username,))
    print(result)
    if result is None:
        print('нет такого пользователя')
        return False
    elif result[1] != password:
        print('Неверный пароль')
        return False
    print(f'Добро пожаловать {result[2]}')
    return True

check_bd()
add_user('user','123456', 'Лев')
login()