from timeit import repeat, timeit

def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'

def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

def func_3():
    num = max(array, key=lambda i: array.count(i))
    count = array.count(num)
    return num, count

def func_4():
    numb = max(array, key=array.count)
    return numb, array.count(numb)

array = [1, 3, 1, 3, 4,4,4,4, 5, 1]
# print(timeit.repeat(stmt='func_1()', setup='array', globals=globals(), repeat=3))
# print(timeit.repeat(stmt='func_2()', setup='array', globals=globals(), repeat=3))
# print(timeit.repeat(stmt='func_3()', setup='array', globals=globals(), repeat=3))
print(timeit("func_1()", globals=globals()))
print(timeit("func_2()", globals=globals()))
print(timeit("func_3()", globals=globals()))
print(timeit("func_4()", globals=globals()))
"""
1.129411515999891
1.4480726289993981  - самый долгий, так как формируется и заполняется новый массив
1.3893508660003135 - быстрее функции с новым массивом, но медленнее 1 и 4 функции, так как применяется лямбда к каждому элементу
0.9404322619993764 - самый быстрый, т.к сразу определяем максимум по двум параметрам
"""
