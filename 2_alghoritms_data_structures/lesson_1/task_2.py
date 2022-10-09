#поиск минимального значения для списка (Сложность алгоритма O(n) - линейная)
def find_min_O1(lst):
    min = lst[0] #O(1)
    for i in range(0, len(lst)): #O(N)
        if lst[i] < min: #O(1)
            min = lst[i] #O(1)
    return min #O(1)

#поиск минимального значения для списка (Сложность алгоритма O(n^2) - квадратичная)
def find_min_O2(lst):
    for i in range(0, len(lst)): #O(N)
        min = lst[i] #O(1)
        for j in range(0, len(lst)): #O(N)
            if lst[j] < min: #O(1)
                min = lst[j] #O(1)
        return min #O(1)




