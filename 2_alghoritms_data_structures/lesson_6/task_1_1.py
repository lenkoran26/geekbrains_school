"""
Оптимизация функции поиска трех организаций с наибольшим доходом
(Урок № 1, Задача № 3)
"""
from memory_profiler import memory_usage
from random import randint
import numpy as np

def profile_memory(func):
    def wripper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Выполнение заняло {mem_diff} Mib')
        return res
    return wripper

@profile_memory
def get_best_profit(info):
    list_info = list(info.items())
    for j in range(len(list_info)):
        for i in range(len(list_info)-1):
            if list_info[i+1][1] > list_info[i][1]:
                buf = list_info[i]
                list_info[i] = list_info[i+1]
                list_info[i+1] = buf
    return list_info[:3]

@profile_memory
def get_best_profit_optimize(info):
    dtype = [('name', 'S15'), ('profit', int)]
    list_info = np.array(list(info.items()), dtype=dtype)
    list_info[::-1].sort(order='profit')
    return list_info[:3]

info = {f'company_{i}': randint(0, 500000) for i in range(1, 10000)}

print(get_best_profit(info))
print(get_best_profit_optimize(info))
"""
Выполнение заняло 0.515625 Mib
[('company_3641', 499988), ('company_4385', 499943), ('company_206', 499917)]

Выполнение заняло 0.25390625 Mib
[(b'company_3641', 499988) (b'company_4385', 499943) (b'company_206', 499917)]

Оптимизированная функция заняла меньше памяти, т.к. использовалась библиотека numpy,
в которой оптимизированы методы обработки больших массивов.
"""