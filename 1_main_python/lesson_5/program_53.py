base = dict()
try:
    with open('textfile_53.txt', 'r') as f_text:
        text = f_text.readlines()
except:
    print('Файл не найден')

"""Заносим данные  в словарь Фамилия : оклад"""
try:
    for line in text:
        entry = line.split()
        base[entry[0]] = entry[1]
except NameError:
    print('Файл не считан')

"""Вывод фамилий сотрудников, чей оклад менее 20000"""
for key,value in base.items():
    if float(value) < 20000:
        print(f'{key} ({value})')

"""Расчет среднего дохода сотрудников"""
income = 0
for value in base.values():
    income += float(value)
try:
    income = income / len(base.values())
except ZeroDivisionError:
    print('Деление на ноль')
print(f'Средний доход сотрудников - {income}')