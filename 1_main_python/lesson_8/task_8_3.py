#Task_8_3

class Myexcept(Exception):
	def __init__(self, message):
		self.mess = message

numbers = list()

print('Enter "stop" for exit')
while True:
	numb = input('Enter the digit ')
	if numb == 'stop':
		break
	try:
		if numb.isdigit() == False:
			raise Myexcept('You don`t enter the digit')
	except Myexcept as err:
		print(err)
		continue
	else:
		numbers.append(numb)

print(numbers)


