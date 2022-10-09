def calc():
    operand = input('Input +,-,*,/ or 0 to EXIT ')
    if operand not in ('+', '-', '*', '/', '0'):
        print('Incorrect operand')
        return calc()
    elif operand == '0':
        print('Goodbay')
        return
    else:
        int_a = input('Enter the first number   ')
        if not int_a.isdigit():
            print(f'{int_a} don`t number')
            return calc()
        int_b = input('Enter the second number ')
        if not int_b.isdigit():
            print(f'{int_b} don`t number')
            return calc()
        if (int_b == '0') and (operand == '/'):
            print('Don`t div by zero')
            return calc()
        if operand == '+':
            print(f'{int_a} {operand} {int_b} = {int(int_a) + int(int_b)}')
            return calc()
        elif operand == '-':
            print(f'{int_a} {operand} {int_b} = {int(int_a) - int(int_b)}')
            return calc()
        elif operand == '/':
            print(f'{int_a} {operand} {int_b} = {int(int_a) / int(int_b)}')
            return calc()
        else:
            print(f'{int_a} {operand} {int_b} = {int(int_a) * int(int_b)}')
            return calc()

calc()