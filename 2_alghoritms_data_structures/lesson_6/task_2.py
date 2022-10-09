from memory_profiler import memory_usage
from random import randint
from functools import reduce
from sys import setrecursionlimit

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

#@profile_memory
def func_count(num, even = 0, odd = 0):
    if num == '':
        return even, odd
    if (int(num[-1]) % 10) % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num[:-1]
    return func_count(num, even, odd)


number_list = reduce(lambda x, y: x + y, [str(randint(0, 9)) for i in range(10)])
func_count(number_list)

"""
...
Выполнение заняло 0.0 Mib
Выполнение заняло 0.0 Mib
Выполнение заняло 0.0 Mib
Выполнение заняло 0.0 Mib
Выполнение заняло 0.0 Mib
Выполнение заняло 0.0 Mib
Выполнение заняло 0.0 Mib
Выполнение заняло 0.0 Mib
Odd - 5, even - 5

Замер памяти выполняется при каждом вызове рекурсивной функции
"""

# измененный вариант декорирования функции,
# чтобы избежать вывод декоратора при каждом вызове рекурсивной функции.
# Теперь вывод используемой памяти происходит один раз,
# так как мы присвоили переменной декорирующую функцию с рекурсивной функцией в виде параметра

decor_func_count = profile_memory(func_count)
even, odd = decor_func_count(number_list)
print(f'Odd - {odd}, even - {even}')

"""
Выполнение заняло 54.515625 Mib
Odd - 4960, even - 5040
"""