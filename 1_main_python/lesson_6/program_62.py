#Task_6_2

class Road:
    _length = 0
    _width = 0
    par_mass = 25
    par_thick = 5
    def __init__(self, len, wid):
        Road._length = len
        Road._width = wid

    def calc(self):
        full_mass = Road._length * Road._width * self.par_mass * self.par_thick / 1000
        return full_mass

par_length = int(input('Введите длину дороги в метрах: '))
par_width = int(input('Введите ширину дороги в метрах: '))
street = Road(par_length, par_width)
print(f'{street.calc()} тонн')