from time import time

def calc_time_decor(func):
    def wrapper(numb):
        start_time = time()
        res = func(numb)
        end_time = time()
        print(func.__name__)
        print(end_time - start_time)
        return res
    return wrapper


@calc_time_decor
def create_list(n):
    my_list = []                #O(1)
    for el in range(n):         #O(N)
        my_list.append(el)      #O(1)
    return my_list              #O(1)

@calc_time_decor
def create_dict(n):
    my_dict = {}                        #O(1)
    for el in range(n):                 #O(N)
        my_dict[el] = 'elem '+str(el)   #O(1)
    return my_dict                      #O(1)

@calc_time_decor
def get_elem_list(list: list):
    for i in list:              #O(N)
        print(i)                #O(1)

#@calc_time_decor
def get_elem_dict(dict: dict):
    for key in dict.keys():     #O(N)
        dict[key] += ' edit'    #O(1)

@calc_time_decor
def del_elem_list(list: list):
    for i in range(len(list)//2):   #O(N)
        list.pop(i)                 #O(N)

@calc_time_decor
def del_elem_dict(dict: dict):
    for i in range(len(dict)//2):   #O(N)
        dict.popitem()              #O(1)

list1 = create_list(1000)
dict1 = create_dict(1000)
get_elem_dict(dict1)
del_elem_list(list1)
del_elem_dict(dict1)
