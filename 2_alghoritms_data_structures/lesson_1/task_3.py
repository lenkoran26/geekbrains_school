profit_company = {
    'ozon': 5456785,
    'avito': 5678945,
    'yamarket': 333222,
    'delivery': 765431,
    'amazon': 1234567,
    'wildber': 652987,
    'korona': 467896,
    'samokat': 688987
}
# O(N Log N)
def get_best_profit_1(info : dict) -> list:
    list_info = list(info.items()) # O(N)
    list_info.sort(key=lambda x: x[1], reverse=True) # O(N Log N)
    return list_info[:3] # O(1)

# O(N^2)
def get_best_profit_2(info: dict) -> list:
    list_info = list(info.items()) # O(N)
    for j in range(len(list_info)): # O(N)
        for i in range(len(list_info)-1): # O(N-1)
            if list_info[i+1][1] > list_info[i][1]: # O(1)
                buf = list_info[i] # O(1)
                list_info[i] = list_info[i+1] # O(1)
                list_info[i+1] = buf # O(1)
    return list_info[:3] # O(1)


print(get_best_profit_1(profit_company))
print(get_best_profit_2(profit_company))

# Эффективнее решение с использованием функции get_best_profit_1, так как сложность используемого алгоритма = O(N Log N)
