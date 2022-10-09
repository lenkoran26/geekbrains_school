from collections import defaultdict
from functools import reduce

# функция получения ключа словаря по значению
def get_value(my_dict, value):
    for k, v in my_dict.items():
        if value == v:
            return k

def sum_hex(num_x, num_y):
    if len(num_y) > len(num_x):
        num_x, num_y = num_y, num_x
    x = list(num_x)[::-1]
    y = list(num_y)[::-1]
    d = 0
    sum = []
    for i in range(len(x)):
        if i > len(y) - 1:
            s = my_dict[x[i]] + d
            d = 0
        else:
            a = my_dict[x[i]] + d
            b = my_dict[y[i]]
            s = a + b
            d = 0
        if s >= 16:
            sum.append(get_value(my_dict, s % 16 + d))
            d += s // 16
        else:
            sum.append(get_value(my_dict, s))
    sum.reverse()
    return sum

def mul_hex(num_x, num_y):
    x = list(num_x)[::-1]
    y = list(num_y)[::-1]
    summa = []
    for i in range(len(x)):
        summa.append(x[i] + '0' * i)
    mul_1 = sum(map(lambda x: int(x,16), summa))
    summa.clear()
    for i in range(len(y)):
        summa.append(y[i] + '0' * i)
    mul_2 = sum(map(lambda x: int(x, 16), summa))
    multiply = list(hex(mul_1 * mul_2)[2:])
    return multiply


my_dict = defaultdict()
hex_symb = '0123456789ABCDEF'
for i in hex_symb:
    my_dict[i] = int(i, 16)

num_x = input('Enter the first hex-number: ').upper()
num_y = input('Enter the second hex-number: ').upper()

print(f'{num_x} + {num_y} = {sum_hex(num_x, num_y)}')
print(f'{num_x} * {num_y} = {mul_hex(num_x, num_y)}')
"""
Enter the first hex-number: 1f4
Enter the second hex-number: 2d
1F4 + 2D = ['2', '2', '1']
1F4 * 2D = ['5', '7', 'e', '4']
"""
