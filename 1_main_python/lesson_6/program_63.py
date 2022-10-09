#Task_6_3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Зарплата': int(wage), 'Премия': int(bonus)}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super(Position, self).__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname + ' - ' + self.position

    def get_total_income(self):
        return self._income.get('Зарплата') + self._income.get('Премия')

worker_1 = Position('Александр', 'Иванов', 'Мэнеджер', '75000', '25000')
worker_2 = Position('Владимир', 'Петров', 'HR', '50000', '20000')

print(worker_1.get_full_name())
print(worker_1.get_total_income())
print(worker_2.get_full_name())
print(worker_2.get_total_income())