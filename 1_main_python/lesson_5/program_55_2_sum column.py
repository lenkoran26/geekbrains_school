#Task_5_5
#Вычисляется сумма чисел в каждой строке и каждом столбце
#Доступен многострочный ввод чисел

from itertools import zip_longest

eof = 'end'
my_list = list()
list_column = list()

print('Введите числа через пробел \n'
                                'Для завершения ввода чисел введите end')

with open('textfile_55_2.txt', 'w') as f_text:
    while True:
        line = input(': ')
        if line.find(eof) != -1:
            f_text.writelines(line[:line.index(eof)])
            break
        else:
            f_text.writelines(line + '\n')

with open('textfile_55_2.txt') as f_text_2:
    text = f_text_2.readlines()
for line in text:
    my_list.append(line.split())

sum_line = 0
sum_col = 0

for line in my_list:
    for el in line:
        sum_line += int(el)
    print(f'{line} = {sum_line}')
    sum_line = 0

list_column = list(zip_longest(*my_list, fillvalue='.'))
for line in list_column:
    for el in line:
        if el != '.':
            sum_col += int(el)
    print(f'Сумма столбца {line} = {sum_col}')
    sum_col = 0
