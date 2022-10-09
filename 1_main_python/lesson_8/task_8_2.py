#Task_8_2

class MyException(Exception):
	def __init__(self, message):
		self.mess = message

num_1 = input('Enter the delimoe ')
num_2 = input('Enter the delitel ')

try:
	if num_2 == 0:
		raise MyException('Division by zero - Error')
except MyException as err:
	print(err)

else:
	print(num_1 / num_2)