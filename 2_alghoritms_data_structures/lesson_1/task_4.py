data_auth = [{'login': 'alex', 'password': 'qwerty', 'is_auth': True},
             {'login': 'john', 'password': '1234', 'is_auth': False},
             {'login': 'mark', 'password': 'asdf', 'is_auth': True},
             {'login': 'bill', 'password': 'zxcv', 'is_auth': False},
]

# функция проверки существования пользователя с именем username
def CheckUsername(username):
    for user_info in data_auth:
        if username == user_info['login']:
            return True
    print('Undefined user')
    return False
# функция аутентификации пользователя и проверки активации учетной записи (1)
def Auth1(username: str, password: str): # 12*O(N)
    for user_info in data_auth: # O(N)
        if (username == user_info['login']) and (user_info['password'] == password) and (user_info['is_auth'] == True): # O(3)
            print('auth is ok') # O(1)
            return False # O(1)
        elif username == user_info['login'] and (user_info['password'] == password) and (user_info['is_auth'] == False): # O(3)
            print('need to activate profil') # O(1)
            return False # O(1)
    print('bad login or password') # O(1)
    return True # O(1)

# функция аутентификации пользователя и проверки активации учетной записи (1)
def Auth2(user, password): # 8*O(N)
    json_user_active = {'login': user, 'password': password, 'is_auth': True} # O(1)
    json_user_inactive = {'login': user, 'password': password, 'is_auth': False} # O(1)
    if json_user_active in data_auth: # O(N)
        print('auth is OK') # O(1)
        return False # O(1)
    elif json_user_inactive in data_auth: # O(N)
        print('need to activate profil') # O(1)
        return False # O(1)
    else:
        print('bad login or password') # O(1)
        return True # O(1)


while True:
    username = input('Введите имя пользователя: ')
    if CheckUsername(username) is True:
        password = input('Введите пароль: ')
        # if Auth_1(username, password) == False:
        if Auth2(username, password) == False:
            break

# функция Auth2 со сложностью 8*O(N) незначительно быстрее функции Auth1 со сложностью 12*O(N)





