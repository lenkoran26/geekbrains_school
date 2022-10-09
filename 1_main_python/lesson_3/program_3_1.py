#Task_3_1

def div_numb(x,y):
    while True:
        if (y == 0):
            print('Деление на 0 невозможно')
            break
        else:
            return x/y

num_1 = int(input('Введите 1-е число '))
num_2 = int(input('Введите 2-е число '))
print(f'{num_1} / {num_2} = {div_numb(num_1,num_2)}')
