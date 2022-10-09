from random import randrange
from timeit import timeit
from statistics import median

def heapify(nums, heap_size, root_index):
    largest_num = root_index
    left_child = (2 * root_index + 1)
    right_child = (2 * root_index + 2)
    if (left_child < heap_size) and (nums[left_child] > nums[largest_num]):
        largest_num = left_child
    if (right_child < heap_size) and (nums[right_child] > nums[largest_num]):
        largest_num = right_child

    if largest_num != root_index:
        nums[root_index], nums[largest_num] = nums[largest_num], nums[root_index]
        heapify(nums, heap_size, largest_num)

def sort_pyramid(my_list):
    n = len(my_list)
    for i in range(n, -1, -1):
        heapify(my_list, n, i)

    for i in range(n-1, 0, -1):
        my_list[i], my_list[0] = my_list[0], my_list[i]
        heapify(my_list, i, 0)

n = 10
m = 2*n+1
my_list = [randrange(-100, 100) for _ in range(m)]

print(f'List:\n{my_list}')

sort_pyramid(my_list)
print(f'Sorted list:\n{my_list}')

my_median = len(my_list) // 2
print(f'Median: {my_list[my_median]}')

time_1 = timeit(stmt='sort_pyramid(my_list)', setup='my_list = [randrange(-100, 100) for _ in range(11)]', globals=globals(), number=1000)
time_2 = timeit(stmt='sort_pyramid(my_list)', setup='my_list = [randrange(-100, 100) for _ in range(101)]', globals=globals(), number=1000)
time_3 = timeit(stmt='sort_pyramid(my_list)', setup='my_list = [randrange(-100, 100) for _ in range(1001)]', globals=globals(), number=1000)
print(f'List of 11 elements: {time_1}')
print(f'List of 101 elements: {time_2}')
print(f'List of 1001 elements: {time_3}')

"""
List:
[96, -65, -46, -48, 70, -19, -60, 45, -18, -11, 59, 4, 35, 45, 63, 33, -41, 23, 81, 51, -86]
Sorted list:
[-86, -65, -60, -48, -46, -41, -19, -18, -11, 4, 23, 33, 35, 45, 45, 51, 59, 63, 70, 81, 96]
Median: 23
List of 11 elements: 0.01763189199846238
List of 101 elements: 0.28183103998890147
List of 1001 elements: 4.379080726997927
"""