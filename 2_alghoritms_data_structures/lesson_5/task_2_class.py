class HexNumber():
    def __init__(self, num):
        #получаем обратный список из чисел, представляющих десятичное представление числа
        self.num = list(str(int(num, 16))[::-1])

    def __add__(self, other):
        #из каждого числа получаем число согласно его разряду (еденицы, десятки, сотни и т.д)
        list_slag = []
        if len(self.num) > len(other.num):
            self.num, other.num = other.num, self.num
        for i in range(0, len(other.num)):
            list_slag.append(int(other.num[i]) * 10 ** i)

        for i in range(0, len(self.num)):
            list_slag[i] += (int(self.num[i]) * 10 ** i)

        summa = list(str(hex(sum(list_slag)))[2:])
        return summa

    def __mul__(self, other):
        if len(self.num) > len(other.num):
            self.num, other.num = other.num, self.num
        sum_mult = []
        addendum = 0
        # умножение чисел в столбик по разрядам
        for i in range(0, len(self.num)):
            addendum = 0
            for j in range(0, len(other.num)):
                addendum += (int(self.num[i]) * 10 ** i) * (int(other.num[j]) * 10 ** j)
            sum_mult.append(addendum)
        mult = list(str(hex(sum(sum_mult)))[2:])
        return mult


x = HexNumber('a2')
y = HexNumber('c4f')
print(x+y)
print(x*y)
#['c', 'f', '1']
#['7', 'c', '9', 'f', 'e']