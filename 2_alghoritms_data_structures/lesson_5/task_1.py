from collections import namedtuple
from statistics import mean

def enter_info():
    org = []
    info = namedtuple('info', ['name', 'profit'])
    try:
        count_org = int(input('Введите количество организаций: '))
    except Exception as err:
        count_org = 0
        print(err)
        exit(0)

    for i in range(1, count_org+1):
        name = input(f'Введите название {i} организации: ')
        profit = input('Введите доход за каждый квартал через запятую: ').split(',')
        profit = list(map(lambda x: int(x), profit))
        info_org = info(name, profit)
        org.append(info_org)
    return org

def get_mean_profit(org_info: list):
    profit = []
    less_profit = {}
    over_profit = {}
    # вычисляем среднее значения дохода всех компаний
    for org in org_info:
        profit += org.profit
    profit_mean = mean(profit)
    # сравниваем средний доход компании с общим средним доходом
    for org in org_info:
        org_profit_mean = mean(org.profit)
        if org_profit_mean >= profit_mean:
            over_profit[org.name] = org_profit_mean
        else:
            less_profit[org.name] = org_profit_mean
    return profit_mean, less_profit, over_profit

org_info = enter_info()
prof, les_prof, over_prof = get_mean_profit(org_info)

print(f'\nСреднее значение прибыли всех фирм - {prof}\n'
      f'фирмы, с прибылью меньше средней - {les_prof}\n'
      f'фирмы, с прибылью больше средней - {over_prof}')

