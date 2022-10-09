#Task_4_6

from itertools import count, cycle

def script_1(start_num, end_num):
    """Функция, генерирующая последовательность при помощи count()"""
    for i in count(start_num):
        print(i, end=' ')
        if i >= end_num:
            break

def script_2(seq,n_seq):
    """Функция, повторяющая элементы последовательности при помощи функции cycle()"""
    n_seq *= len(seq)
    for el in cycle(seq):
        print(el, end='')
        if n_seq == 1:
            break
        n_seq -= 1

start_n = int(input('Введите начальное число последовательности '))
end_n = int(input('Введите конечное число последовательности '))

print(f'Итерация от {start_n} до {end_n}: ')
script_1(start_n, end_n)

sequence = ['A','B','C','D']
#количество повторений последовательности num_seq
num_seq = 4
print(f'\nПоследовательность: {sequence}')
print(f'Количество повторений последовательности: {num_seq}')
script_2(sequence, num_seq)