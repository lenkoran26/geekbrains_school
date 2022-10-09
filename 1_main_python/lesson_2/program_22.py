my_list = list()
n = 6

for i in range(0,n):
    my_list.append(input(f'Введите {i+1}-й из {n} элемент списка '))
print(f'Исходный список - {my_list}')

for i in range(0,len(my_list)-1,2):
    my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
    
print(f'Измененный список - {my_list}')