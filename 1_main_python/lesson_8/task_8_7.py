#Task_8_7

class Complex():
	def __init__(self, a, b):
		self.re = a
		self.im = b
		self.j = 'j'
		print(f'Complex digit is {self.re} + {self.im}{self.j}')

	def __add__(self, other):
		return f'{(self.re + other.re)} + {(self.im + other.im)}{self.j}'

	def __mul__(self, other):
		return f'{self.re * other.re - self.im * other.im} + {self.re * other.im + self.im * other.re}{self.j}'


num_1 = Complex(2, 3)
num_2 = Complex(5, 7)
print(num_1 + num_2)
print(num_1 * num_2)