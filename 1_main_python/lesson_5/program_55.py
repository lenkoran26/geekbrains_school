#Task_5_5

numbers = input('Введите набор чисел через пробел: ')
sum = 0
with open('textfile_55.txt','w+') as f_text:
    f_text.writelines(numbers)
    f_text.seek(0)
    list_numbers = f_text.readlines()
    for line in list_numbers:
        array_numbers = line.split()
        try:
            for i in array_numbers:
                sum += int(i)
        except ValueError:
            print(f'{i} не является числом')


print(sum)