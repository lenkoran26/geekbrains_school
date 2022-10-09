#Task_5_1
with open('my_file.txt', 'w') as my_f:
    while True:
        text = input('Введите очередную строку: \n'
                     'для завершения ввода введите пустую строку \n')
        if text == '':
            break
        my_f.write(text + '\n')

