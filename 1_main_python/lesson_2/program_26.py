goods = {}              #словарь для текущего товара
analiz = {}             #словарь для аналитики
base = list()           #список характеристик товаров
struct = list()         #список всех товаров
h=1                     #номер характеристики товара для вывода
#Ввод характеристик товаров
while True:
    word = input(f'Введите {h} характеристику товара \nВведите "end", чтобы завершить ввод \n')
    if word == 'end': break
    else:
        base.append(word)
        h+=1

counter = 0             #позиция товара в списке
flag = True             #флаг завершения ввода

#Ввод информации о товарах
while True:
    counter += 1
    for char in base:
        x = input(f'Ввод информации о {counter} товаре \n Введите {char}  \n Введите "end", чтобы завершить ввод \n')
        if (x == 'end') :
            flag = False
            break
        else:
            goods[char] = x
            y = goods.copy()
    if (flag == False):
        break
    struct.append(tuple((counter, y)))

#Вывод всех товаров
for tovar in struct:
    print(tovar)

#Сбор аналитической информации
for name in base:
    data = []
    for good in struct:
        data.append(good[1].get(name))
    analiz[name] = data

#Вывод аналитической информации
for key,value in analiz.items():
    print(key,value)