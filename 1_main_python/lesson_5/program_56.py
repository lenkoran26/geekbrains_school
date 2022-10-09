my_list = list()
my_dict = dict()

try:
    with open('textfile_56.txt') as f_text:
        table = f_text.readlines()
        for line in table:
            my_list.append(line.split())
except FileNotFoundError:
    print('Файл не найден')

sum = 0
for el in my_list:
    ind_1 = el[0].index(':')

    for i in range(1, len(el)):
        if el[i] != '-':
            ind_2 = el[i].index('(')
            sum += int(el[i][:ind_2])

    my_dict[el[0][:ind_1]] = sum
    sum = 0
print(my_dict)

