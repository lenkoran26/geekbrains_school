#Task_7_2

class Clothes:
    all_cloth = 0
    def calc(self):
        return self.all_cloth

class Coat(Clothes):
    def __init__(self, V):
        self.size = float(V)
    def calc(self):
        result = round(self.size / 6.5 + 0.5, 2)
        Clothes.all_cloth += result
        return f'Объем ткани на текущий элемент (костюм) - {result} \n' \
               f'Общее количество ткани - {self.all_cloth}'

class Costume(Clothes):
    def __init__(self, H):
        self.height = float(H)
    def calc(self):
        result = round(self.height * 2 + 0.3)
        Clothes.all_cloth += result
        return f'Объем ткани на текущий элемент (пальто) - {result} \n' \
               f'Общее количество ткани - {self.all_cloth}'

costume_1 = Costume(3)
print(costume_1.calc())
coat_1 = Coat(140)
print(coat_1.calc())
costume_2 = Costume(5)
coat_2 = Coat(120)
print(costume_2.calc())
print(coat_2.calc())