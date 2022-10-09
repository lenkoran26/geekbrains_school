#Task_3_2

def notebook(name,family,date,city,email,phone):
    print(f'{name} {family} {date} {city} {email} {phone}')

def check_email(email):
    """Функция проверки корректности ввода email"""

    if '@' not in email:
        print('некорректный адрес')
        return 'invalid_email'
    elif (email.index('@') == 0) | (email.index('@') == len(email)-1):
        print('нет логина или домена')
        return 'invalid_email'
    elif (email.index('.') != len(email)-3) & (email.index('.') != len(email)-4):
        print('нет домена')
        return 'invalid_email'
    else:
        return email

def check_phone(phone):
    """Функция проверки корректности ввода номера телефона"""

    valid_chr = ['0','1','2','3','4','5','6','7','8','9']
    for num in phone:
        if num not in valid_chr:
            print('некорректный номер')
            return 'invalid_number'
    return phone

def check_date(date):
    """Функция проверки корректности ввода года рождения"""

    valid_chr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for num in date:
        if (num not in valid_chr) | (len(date) > 4):
            print('некорректный год рождения')
            return 'invalid_date'
    return date

arg_name = input('Введите имя: ')
arg_family = input('Введите фамилию: ')
arg_date = input('Введите год рождения: ')
arg_date = check_date(arg_date)
arg_city = input('Введите город проживания: ')
arg_email = input('Введите e-mail: ')
arg_email = check_email(arg_email)
arg_phone = input('Введите телефон: ')
arg_phone = check_phone(arg_phone)

notebook(name=arg_name,   family=arg_family,
         date=arg_date,   city=arg_city,
         email=arg_email, phone=arg_phone)

