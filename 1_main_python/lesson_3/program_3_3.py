#Task_3_3

def my_func(a,b,c):
    numbers = [a,b,c]
    numbers.remove(min(numbers))
    return sum(numbers)

x,y,z = map(int,input('Введите три числа через пробел: ').split())
print(f'Сумма двух наибольших чисел - {my_func(x,y,z)}')

