proceeds = float(input("Введите значение прибыли - "))
cost = float(input("Введите значение издержек - "))
saldo = proceeds - cost

if saldo > 0:
    print("Фирма получает прибыль")
    print(f'Рентабельность = {"%.2f" % ((saldo)/proceeds * 100)}')

elif saldo < 0:
    print("Фирма несет убытки")

elif saldo == 0:
    print("Стабильность")

am_workers = int(input("Введите количество сотрудников - "))
print(f'Прибыль в расчете на одного сотрудника = {"%.2f"%((saldo)/am_workers)}')