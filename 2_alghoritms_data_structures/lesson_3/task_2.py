import sqlite3
import hashlib
from uuid import uuid4

# регистрация нового пользователя
def register_user():
    username = input('Введите имя пользователя: ')
    while True:
        password = input('Введите пароль: ')
        repeat_password = input('Повторите введенный пароль: ')
        if password != repeat_password:
            print('Пароли не совпадают! Повторите ввод!')
        else:
            break
    # вычисление соли
    salt = uuid4().hex.encode('utf-8')
    # создание хэша пароля с солью
    hash_password = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()
    return username, hash_password, salt

# добавление нового пользователя в БД
def add_user(username, hash_passwd, salt):
    try:
        user_info = (username, hash_passwd, salt)
        cur.execute("""INSERT INTO users
        (login, hash, salt) VALUES
        (?,?,?)
        """, user_info)
        conn.commit()
        print(f'Пользователь {username} успешно создан')
        print(f'Хэш пароля - {hash_passwd}')
    except Exception as err:
        if err.args[0] == 'UNIQUE constraint failed: users.login':
            print('Такой пользователь уже существует')


# аутентификация пользователя
def authorization():
    while True:
        username = input('Введите имя пользователя: ')
        # проверка существования пользователя
        sql_query = cur.execute("SELECT * FROM users WHERE login=?", (username,))
        query = sql_query.fetchone()
        # вычисление хэша введенного пароля и проверка с соответствующим в БД
        if query:
            password = input('Введите пароль: ')
            hash_pass_store = query[2]
            solt_store = query[3]
            hash_pass = hashlib.sha256(password.encode('utf-8')+solt_store).hexdigest()
            if hash_pass == hash_pass_store:
                print(f'Пользователь {username} успешно аутентифицирован')
                print(f'Хэш введенного пароля - {hash_pass}, хэш из БД - {hash_pass_store}')
                break
            else:
                print('Неправильный пароль! Повторите еще раз!')
        else:
            print(f'Пользователь {username} не существует')


conn = sqlite3.connect('mydb.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   id INTEGER PRIMARY KEY,
   login VARCHAR(50) NOT NULL UNIQUE,
   hash TEXT NOT NULL,
   salt TEXT NOT NULL);
""")
conn.commit()

while True:
    print("""Выберете необходимое действие (введите 0, 1 или 2)\n
1. Добавить нового пользователя\n
2. Войти в систему\n
0. Выход\n """)
    case = input('-> ')
    if case == '1':
        username, hash_pas, salt = register_user()
        add_user(username, hash_pas, salt)
        break
    elif case == '2':
        authorization()
        break
    elif case == '0':
        break
    break

conn.close()






