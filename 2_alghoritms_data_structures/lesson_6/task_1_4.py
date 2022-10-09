"""
Оптимизация функции, возвращающей число в обратном порядке
Урок № 4, задача № 3
"""
from memory_profiler import memory_usage
from functools import reduce
from random import randint

def profile_memory(func):
    def wripper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Выполнение заняло {mem_diff} Mib')
        return res, mem_diff
    return wripper

# переписали функцию для возможности работы с числом в строковом виде (чтобы увеличить размер числа)
@profile_memory
def revers_2(enter_num):
    reverse_num = ''
    while enter_num != '':
        num = enter_num[-1]
        reverse_num = reverse_num + num
        enter_num = enter_num[:-1]
    return reverse_num

@profile_memory
def revers_2_optim(enter_num):
    for i in enter_num[::-1]:
        yield i

num_str = reduce(lambda x, y: x + y, [str(randint(0, 9)) for i in range(1000000)])

print('Функция до оптимизации:')
revers_2(num_str)

print('Функция-генератор:')
my_gen, mem_diff = revers_2_optim(num_str)

print('Опустошение генератора:')
temp_str = ''
m1 = memory_usage()

for i in my_gen:
    temp_str += i

m2 = memory_usage()
print(f'{m2[0] - m1[0]} Mib')

"""
Функция до оптимизации:
Выполнение заняло 0.76953125 Mib
Функция-генератор:
Выполнение заняло 0.0 Mib
Опустошение генератора:
0.0 Mib

И генерирующая функция, и процесс опустошения генератора не заняли память,
что показывает их оптимальное использование, когда весь результат иетартора не нужен сразу
"""