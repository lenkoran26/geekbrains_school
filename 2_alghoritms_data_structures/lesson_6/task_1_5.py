"""
Оптимизация функции, возвращающей наиболее часто встречающийся элемент массива
Урок № 4, задача № 4
"""
from memory_profiler import memory_usage
from random import randint
from collections import Counter

def profile_memory(func):
    def wripper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Выполнение заняло {mem_diff} Mib')
        return res, mem_diff
    return wripper

@profile_memory
def func_1(my_list):
    new_array = []
    for el in my_list:
        count2 = my_list.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = my_list[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

@profile_memory
def func_2(my_list):
    dict_of_count = Counter(my_list)
    num = dict_of_count.most_common()[0][0]
    count = dict_of_count.most_common()[0][1]
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {count} раз(а)'

my_list = [randint(0,9) for i in range(10000)]
print('Функция до оптимизации:')
func_1(my_list)
print('Функция после оптимизации:')
func_2(my_list)

"""
Функция до оптимизации:
Выполнение заняло 0.4375 Mib
Функция после оптимизации:
Выполнение заняло 0.0 Mib

Функция, использующая метод Counter из коллекции, заняла меньше памяти, 
чем функция, использующая массив 
"""