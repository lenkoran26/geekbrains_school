#Task_4_7_2
#Вариант, при котором генератор выдает циклу числа для перемножения

def fact(n):
    for i in range(0, n+1):
        if i == 0:
            yield 1
        else:
            yield i

n = int(input("Введите число, для которого необходимо вычислить факториалы - "))
f = 1
j = 0
for i in fact(n):
    f = f*i
    print(f'{j}! = {f}')
    j += 1
