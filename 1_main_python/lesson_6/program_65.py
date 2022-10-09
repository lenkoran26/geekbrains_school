#Task_6_5

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super(Pen, self).__init__(title)
        print(f'Инструмент {self.title}')
    def draw(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def __init__(self, title):
        super(Pencil, self).__init__(title)
        print(f'Инструмент {self.title}')
    def draw(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def __init__(self, title):
        super(Handle, self).__init__(title)
        print(f'Инструмент {self.title}')
    def draw(self):
        print('Запуск отрисовки маркером')
pen = Pen('Ручка')
pen.draw()

penc = Pencil('Карандаш')
penc.draw()

handle = Handle('Маркер')
handle.draw()

