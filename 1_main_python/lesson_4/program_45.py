#Task_4_5

from functools import reduce

def my_func():
    for num in range(100,1001):
        if num % 2 == 0:
            yield num

mult = reduce(lambda x,y:x*y,list(my_func()))
print(mult)