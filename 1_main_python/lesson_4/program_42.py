#Task_4_2

list_numb = [21, 43, 320, 54, 65, 71, 43, 26, 66, 2, 132]
new_list_numb = (list_numb[i] for i in range(1, len(list_numb)) if list_numb[i-1] < list_numb[i])

print(list(new_list_numb))