#Task_4_4

def my_func(list_a):
    for num in list_a:
        if not(list_a.count(num) > 1):
            yield num

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(list(my_func(my_list)))
