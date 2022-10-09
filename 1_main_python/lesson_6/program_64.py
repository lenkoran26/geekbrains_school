#Task_6_4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police == True:
            self.name += ' (полицейская машина)'

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed} км/ч')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(TownCar, self).__init__(speed, color, name, is_police)
    
    def show_speed(self):
        if int(self.speed) > 60:
            print(f'Скорость {self.name} - {self.speed}. Превышение скорости свыше 60')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(SportCar, self).__init__(speed, color, name, is_police)
        
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(WorkCar, self).__init__(speed, color, name, is_police)
    
    def show_speed(self):
        if int(self.speed) > 40:
            print(f'Скорость {self.name} - {self.speed}. Превышение скорости свыше 40')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super(PoliceCar, self).__init__(speed, color, name, is_police)

corvet = PoliceCar(60,'white-blue','dodge',True)
mazda = SportCar(220, 'red', 'rx-8', False)
toyota = WorkCar(100, 'black', 'camry', False)
honda = TownCar(80, 'white', 'civic', False)

corvet.go()
mazda.go()
toyota.go()
honda.go()

corvet.turn('налево')
mazda.turn('направо')
honda.show_speed()
toyota.show_speed()
mazda.show_speed()