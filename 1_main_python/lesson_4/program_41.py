#Task_4_1

import argparse
parser = argparse.ArgumentParser(description='Расчет зарплаты сотрудника')
parser.add_argument("-hr", "--hours", type=float, default=12.0, help="Количество часов, по умолчанию - 12")
parser.add_argument("-t", "--tarif", type=float, default=1000.0, help="Ставка в час, по умолчанию - 1000")
parser.add_argument("-p", "--prize", type=float, default=1500.0, help="Премия, по умолчанию - 1500")

args = parser.parse_args()
salary = args.hours * args.tarif + args.prize
print(f'Зарплата = {round(salary,3)}')