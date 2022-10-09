#Task_3_6

def my_func(str_numb,index_end):
    global summa

    for i in str_numb:
        if (i == index_end):
            str_numb = str_numb[0:str_numb.index(i)]
            print('Функция завершена')
    seq_num = map(int,str_numb.split())

    summa += sum(seq_num)
    
    return summa

ind_off='e'
summa = 0
print("Введите числа через пробел ")

while True:
    s = input()
    print(f' {my_func(s,ind_off)}')