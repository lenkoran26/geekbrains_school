from timeit import timeit
from statistics import median
from random import randrange

n = 10
m = 2*n+1
my_list = [randrange(-100, 100) for _ in range(m)]

median_of_list = median(my_list)
print(f'Median of list: {my_list}\n{median_of_list}')

time_1 = timeit(stmt='median(my_list)', setup='my_list = [randrange(-100, 100) for _ in range(11)]', globals=globals(), number=1000)
time_2 = timeit(stmt='median(my_list)', setup='my_list = [randrange(-100, 100) for _ in range(101)]', globals=globals(), number=1000)
time_3 = timeit(stmt='median(my_list)', setup='my_list = [randrange(-100, 100) for _ in range(1001)]', globals=globals(), number=1000)
print(f'List of 11 elements: {time_1}')
print(f'List of 101 elements: {time_2}')
print(f'List of 1001 elements: {time_3}')

"""
Median of list: [49, -99, -12, 69, -48, -51, -37, -54, 75, -99, 22, 41, -87, -46, -12, 42, -84, -45, -32, 22, 29]
-32
List of 11 elements: 0.0005372210289351642
List of 101 elements: 0.0028038389864377677
List of 1001 elements: 0.08165555796585977

Выводы: 
1. быстрее всех отработала встроенная в модуль statistics функция median, 
2. следующая по скорости функция сортировки методом кучи,
3. медленнее всего выполнилась написанная функция поиска без сортировки
    (квадратичный поиск и подсчет элементов больших и меньших медианы)
"""