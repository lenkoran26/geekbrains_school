#Task_4_7

def fact(n):
    f = 1

    for i in range(0, n+1):
        if i==0: i=1
        f = f * i
        yield f

n = int(input("Введите число, до которого необходимо вычислить факториалы - "))
i = 0
for el in fact(n):
    print(f'{i}! = {el}')
    i += 1