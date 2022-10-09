"""
Оптимизация функции, возвращающей квадраты четных чисел при помощи генератора
Урок № 4, задача № 1
"""
from memory_profiler import memory_usage

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
def func_1(nums):
    new_arr = []
    for i in nums:
        if i % 2 == 0:
            new_arr.append(i ** 2)
    return new_arr

@profile_memory
def func_2(nums):
    for i in nums:
        if i % 2 == 0:
            yield i ** 2

my_new_list = []
my_list = [i for i in range(10000000)]

print('Функция до оптимизации генератором:')
func_1(my_list)

print('Функция, возвращающая генератор:')
func_2_gen, mem_diff = func_2(my_list)

print('Использование памяти при опустошении генератора (элементы, выдаваемые генератором, заносятся в новый массив):')
m1 = memory_usage()
for i in func_2_gen:
    my_new_list.append(i)
m2 = memory_usage()
print(f'{m2[0] - m1[0]} Mib')

"""
Функция до оптимизации генератором:
Выполнение заняло 193.06640625 Mib
Функция, возвращающая генератор:
Выполнение заняло 0.0 Mib
Использование памяти при опустошении генератора (элементы, выдаваемые генератором, заносятся в новый массив):
192.71875 Mib

Вывод: как таковой, генератор не занимает много памяти. Полезен, когда мы хотим постепенно получать из него элементы.
Но если мы сразу хотим получить все элементы в генераторе, то выигрыш в памяти не так значителен
"""