"""
Оптимизация функции подсчета четных и нечетных элементов последовательности
(Урок № 2, Задача № 2)
"""
from memory_profiler import memory_usage
from random import randint
from functools import reduce
from sys import setrecursionlimit

# изменили глубину стека вызовов
setrecursionlimit(100000)

def profile_memory(func):
    def wripper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Выполнение заняло {mem_diff} Mib')
        return res
    return wripper

# переписали функцию из урока 2, задачи 2 для работы с большим числом в виде строки
def func_count(num, even = 0, odd = 0):
    if num == '':
        return even, odd
    if (int(num[-1]) % 10) % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num[:-1]
    return func_count(num, even, odd)

# оптимизированная функция, использующая filter
@profile_memory
def func_count_2(number_str: str):
    list_numbers = list(number_str)
    odd = list(filter(lambda x: int(x) % 2 == 0, list_numbers))
    even = list(filter(lambda x: int(x) % 2 != 0, list_numbers))
    return len(odd), len(even)

number_str = reduce(lambda x, y: x + y, [str(randint(0, 9)) for i in range(10000)])

# измененный вариант декорирования функции,
# чтобы избежать вывод декоратора при каждом вызове рекурсивной функции.
# Теперь вывод используемой памяти происходит один раз

decor_func_count = profile_memory(func_count)
even, odd = decor_func_count(number_str)
print(f'Odd - {odd}, even - {even}')

even, odd = func_count_2(number_str)
print(f'Odd - {odd}, even - {even}')

"""
Рекурсивный вариант:
Выполнение заняло 54.65625 Mib
Odd - 4945, even - 5055

Вариант с функцией filter
Выполнение заняло 0.0 Mib
Odd - 4945, even - 5055

Для числа, состоящего из 10000 цифр вариант с filter показал значительное превосходство в сравнении с рекурсией
Для числа, состоящего из 100000 цифр вариант с filter показал:
Выполнение заняло -0.03515625 Mib
Odd - 50186, even - 49814
Рекурсия с таким количеством цифр не справилась
"""