from random import randrange
from timeit import timeit

def sort_list_flag(my_list: list):
    for i in range(len(my_list)):
        flag_sort = True
        for j in range(len(my_list)-1):
            if my_list[j] < my_list[j+1]:
                flag_sort = False
                buf = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = buf
        if flag_sort == True:
            return i, my_list

def sort_list(my_list: list):
    for i in range(len(my_list)):
        for j in range(len(my_list)-1):
            if my_list[j] < my_list[j+1]:
                buf = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = buf
    return my_list

n = 10
my_list = [randrange(-100, 100) for _ in range(n)]
print(f'Original list:\n{my_list}')

i, my_list_sort = sort_list_flag(my_list)
my_list_sort_2 = sort_list(my_list)

print(f'count iterations = {i}\n Sorted list: \n{my_list_sort}')
print(my_list_sort_2)

time_1 = timeit(stmt='sort_list_flag(my_list)', setup='my_list = [randrange(-100, 100) for _ in range(100)]', globals=globals(), number=1000)
time_2 = timeit(stmt='sort_list(my_list)', setup='my_list = [randrange(-100, 100) for _ in range(100)]', globals=globals(), number=1000)
print(f'Sorting with flag\n{time_1}')
print(f'Sorting \n{time_2}')

"""
Original list:
[-28, 17, -100, 84, 50, 14, -68, -89, -28, 7]
count iterations = 5
 Sorted list: 
[84, 50, 17, 14, 7, -28, -28, -68, -89, -100]
[84, 50, 17, 14, 7, -28, -28, -68, -89, -100]
Sorting with flag
0.015022702020360157
Sorting 
0.7237487389938906

Выводы: быстрее выполнилась функция, улучшенная флагом отсортированного массива.
Наибольшее преимущество она дает, когда массив практически отсортирован. 
Наименьшее преимущество - когда массив отсортирован в порядке обратном нужному
count iterations = 5 - показывает, за сколько итераций был обработан массив. 
В данном случае функция закончила свое выполнение на 5 из 10 шагов, что значительно сэкономило время
"""