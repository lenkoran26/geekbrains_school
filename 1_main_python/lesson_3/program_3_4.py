#Task_3_4

def my_func(x,y):
    """ Решение через цикл"""
    f_sqrt = 1
    for i in range(abs(y)):
        f_sqrt = f_sqrt*x

    """ Решение через ** """
    f_sqrt_2 = 1/(x**abs(y))

    return 1/f_sqrt, f_sqrt_2

base = float(input(f'Введите основание - '))
power = int(input(f'Введите степень - '))

out_1,out_2 = (my_func(base,power))
print(f'Решение через ** - {out_1}, решение через цикл - {out_2}')