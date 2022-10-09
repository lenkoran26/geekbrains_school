from random import randrange
from timeit import timeit
from statistics import median

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

n = 100
m = 2*n+1
my_list = [randrange(-100, 100) for _ in range(m)]

print(median(my_list))

print(search_median(my_list))
pass