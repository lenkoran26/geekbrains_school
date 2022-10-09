from timeit import timeit
import numpy as np

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num):
    revers_num = ''.join(reversed(str(enter_num)))
    return revers_num

t1 = timeit('revers(enter_num)', setup='enter_num=123456', globals=globals())
t2 = timeit('revers_2(enter_num)', setup='enter_num=123456', globals=globals())
t3 = timeit('revers_3(enter_num)', setup='enter_num=123456', globals=globals())
t4 = timeit('revers_4(enter_num)', setup='enter_num=123456', globals=globals())

print(f'Время выполнения функции, использующую рекурсию = {t1}')
print(f'Время выполнения функции, использующую цикл While = {t2}')
print(f'Время выполнения функции, использующую срезы строк = {t3}')
print(f'Время выполнения функции, использующую функцию reversed = {t4}')
"""
Время выполнения функции, использующую рекурсию = 0.8729916119991685
Время выполнения функции, использующую цикл While = 0.5415837269993062
Время выполнения функции, использующую срезы строк = 0.16171313099948748
Время выполнения функции, использующую функцию reversed = 0.326104669000415
"""

"""
Вывод: самая быстрая функция, построенная на срезах, т.к больше нет никаких операций и циклов
На втором месте функция, использующая встроенную функцию reversed. 
В ней выолняется два действия: 
1. Возвращение итерируемого объекта из символов в обратном порядке
2. Соединение этих символов в строку при помощи встроенного метода join
"""