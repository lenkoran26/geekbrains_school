from random import randrange
from timeit import timeit

def search_median(my_list):
    for i in range(len(my_list)):
        more_median = []
        less_median = []
        equal_median = []
        my_median = my_list[i]
        for j in range(len(my_list)):
            if i == j:
                continue
            if my_list[j] > my_median:
                more_median.append(my_list[j])
            elif my_list[j] < my_median:
                less_median.append(my_list[j])
            else:
               equal_median.append(my_list[j])
        if len(less_median) == len(more_median):
            return my_median
        if abs(len(more_median) - len(less_median)) <= len(equal_median):
            if len(more_median) > len(less_median):
                more_median, less_median = less_median, more_median
            k = len(less_median) - len(more_median)
            for _ in range(k):
                more_median.append(equal_median.pop())
            if len(less_median) == len(more_median):
                return my_median

n = 10
m = 2*n+1
my_list = [randrange(-100, 100) for _ in range(m)]
print(f'List:\n{my_list}')

my_median = search_median(my_list)
print(f'Median of list: {my_median}')

time_1 = timeit(stmt='search_median(my_list)', setup='my_list = [randrange(-100, 100) for _ in range(11)]', globals=globals(), number=1000)
time_2 = timeit(stmt='search_median(my_list)', setup='my_list = [randrange(-100, 100) for _ in range(101)]', globals=globals(), number=1000)
time_3 = timeit(stmt='search_median(my_list)', setup='my_list = [randrange(-100, 100) for _ in range(1001)]', globals=globals(), number=1000)
print(f'List of 11 elements: {time_1}')
print(f'List of 101 elements: {time_2}')
print(f'List of 1001 elements: {time_3}')

"""
List:
[-57, 19, 42, -20, -69, -58, -56, 46, -32, 91, -52, 34, -55, -74, -77, 96, -40, 64, -88, 64, 70]
Median of list: -32
List of 11 elements: 0.0018720080006460194
List of 101 elements: 0.24674903400045878
List of 1001 elements: 15.16493192300004
"""