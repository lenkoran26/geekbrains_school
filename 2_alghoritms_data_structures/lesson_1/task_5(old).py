class Bowls():
    # инициализация стопки тарелок и массива стопок
    def __init__(self):
        self.stack_of_bowls = []
        self.array_of_stack_bowls = []

    # добавление тарелки в стопку
    def add_to_stack(self, elem):
        self.stack_of_bowls.append(elem)

    def get_value(self):
        return self.stack_of_bowls[len(self.stack_of_bowls)-1]

    def pop_out(self):
        return self.stack_of_bowls.pop()

    # проверка заполненности стопки
    def is_full(self, size):
        if len(self.stack_of_bowls) >= size:
            return True

    # добавление стопки в массив стопок
    def add_to_array_bowls(self, stack):
        self.array_of_stack_bowls.append(stack)

    # получение размера массива стопок
    def size_of_array_bowls(self):
        return len(self.array_of_stack_bowls)

count_of_bowls = 30 # общее количество тарелок
blows = Bowls()
blows.stack_of_bowls = [1,2,3,4,5,6,7,8,9,10]
size_of_stack = 7   # размер стопки тарелок

obj_stack = Bowls()

for i in range(1, count_of_bowls+2):
    # если тарелки закончились, последнюю стопку добавляем в массив
    if i == count_of_bowls+1:
        obj_stack.add_to_array_bowls(obj_stack.stack_of_bowls.copy())
        obj_stack.stack_of_bowls.clear()
    # полную стопку добавляем в массив стопок и начинаем новую
    if obj_stack.is_full(size_of_stack):
        obj_stack.add_to_array_bowls(obj_stack.stack_of_bowls.copy())
        obj_stack.stack_of_bowls.clear()
        obj_stack.add_to_stack(i)

    else:
        # добавление тарелки в незаполненную стопку
        obj_stack.add_to_stack(i)


print(f'Размер формируемых стопок - {size_of_stack} тарелок')
print(f'Количество полученных стопок с тарелками - {obj_stack.size_of_array_bowls()}')
print("Полученные стопки:")
print(obj_stack.array_of_stack_bowls)
