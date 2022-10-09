#Task_6_1

from time import sleep

class TrafficLight():
    __color = {'красный': 7, 'желтый': 2, 'зеленый': 10}

    def running(self):
        for color, time in self.__color.items():
            print(color)
            timer = time
            while timer != 0:
                print(timer, end=' ')
                sleep(1)
                timer -= 1
            print()

t_l = TrafficLight()
t_l.running()
