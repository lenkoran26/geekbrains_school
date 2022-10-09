from timeit import timeit
import timeit
import numpy as np

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_set = set()
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_set.add(i)
    return new_set

def func_3(nums):
    return [i for i, element in enumerate(nums) if element % 2 == 0]

def func_4(nums):
    my_list = np.arange(nums)
    return my_list[my_list % 2 == 0]

t1 = timeit.repeat(stmt='func_1(nums)', setup='nums = [i for i in range(1000)]', globals=globals(), number=10000, repeat=3)
t2 = timeit.repeat(stmt='func_2(nums)', setup='nums = [i for i in range(1000)]', globals=globals(), number=10000, repeat=3)
t3 = timeit.repeat(stmt='func_3(nums)', setup='nums = [i for i in range(1000)]', globals=globals(), number=10000, repeat=3)
t4 = timeit.repeat(stmt='func_4(nums)', setup='nums=1000', globals=globals(), number=10000, repeat=3)

print(t1)
print(t2)
print(t3)
print(t4)
"""
[0.5338282839998101, 0.5187006300002395, 0.47776088799992067] - вариант с list
[0.4877168759999222, 0.4872596190002696, 0.48621108900033505] - вариант с set (особо ничего не изменилось)
[0.3917622060002941, 0.39087641399964923, 0.3937220200000411] - вариант со списковым включением (заметно быстрее)
[0.08544565100010004, 0.08476915300025212, 0.08445146299982298] - вариант с использование библиотеки numpy (очень быстро)
"""