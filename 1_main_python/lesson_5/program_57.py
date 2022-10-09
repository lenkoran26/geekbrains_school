import json
my_list = list()
dict_firms = dict()
dict_average = dict()
list_from_json = list()
ind_l = 0
average_profit = 0
i_positive_prof = 0

"""Создание словаря Фирма : прибыль"""
with open('textfile_57.txt') as my_file:
    table = my_file.readlines()
for line in table:
    my_list.append(line.split())
    dict_firms[my_list[ind_l][0]] = float(my_list[ind_l][2]) - float(my_list[ind_l][3])
    ind_l += 1
my_list.clear()

"""Вычисление среднего дохода фирм"""
for value in dict_firms.values():
    if value > 0:
        average_profit += value
        i_positive_prof += 1
average_profit = average_profit / i_positive_prof
dict_average['average profit'] = round(average_profit,2)

my_list.append(dict_firms)
my_list.append(dict_average)
print(my_list)

"""Преобразование из List в JSON"""
with open('jsonfile57.json','w') as file_json:
    json.dump(my_list, file_json, ensure_ascii=False)

"""Преобразование из JSON в List"""
with open('jsonfile57.json', 'r') as file_json_2:
    list_from_json = json.load(file_json_2)
print(list_from_json)