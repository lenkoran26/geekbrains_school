class Bowls():
    # инициализация стопки тарелок и массива стопок
    def __init__(self, stack_of_bowls=[]):
        self.stack_of_bowls = stack_of_bowls
        self.array_of_stack_bowls = []

    # добавление тарелки в стопку
    def add_to_stack(self, elem):
        self.stack_of_bowls.append(elem)

    # получение верхнего элемента
    def get_value(self):
        return self.stack_of_bowls[len(self.stack_of_bowls)-1]

    # получение и удаление верхнего элемента
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

bowls = Bowls([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
obj_stack = Bowls()
print(f'Исходная стопка тарелок: {bowls.stack_of_bowls}')
print(f'Количество тарелок в исходной стопке - {len(bowls.stack_of_bowls)} тарелок')
size_of_stack = 6   # размер стопки тарелок

while len(bowls.stack_of_bowls) != 0: # пока тарелки в исходной стопке не закончились
    if not obj_stack.is_full(size_of_stack): # если текущая стопка тарелок не заполнена
        # добавление тарелки в незаполненную стопку
        bowl = bowls.pop_out()
        obj_stack.add_to_stack(bowl)

    else: #полную стопку добавляем в массив стопок и начинаем новую
        obj_stack.add_to_array_bowls(obj_stack.stack_of_bowls.copy())
        obj_stack.stack_of_bowls.clear()
        bowl = bowls.pop_out()
        obj_stack.add_to_stack(bowl)

# добавление оставшихся тарелок в стопку
obj_stack.add_to_array_bowls(obj_stack.stack_of_bowls.copy())
obj_stack.stack_of_bowls.clear()

print(f'Размер формируемых стопок - {size_of_stack} тарелок')
print(f'Количество полученных стопок с тарелками - {obj_stack.size_of_array_bowls()}')
print("Полученные стопки:")
print(obj_stack.array_of_stack_bowls)


