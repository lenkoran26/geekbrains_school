#Task_8_4-6

class Orgtech():

	def add_tech(self):
		"""Добавить технику на склад"""

		name = input('Введите название: ')
		model = input('Введите модель: ')
		try:
			count = input('Введите количество: ')
			price = input('Введите стоимость: ')
			if not(count.isdigit() == True & price.isdigit() == True):
				raise TypeError
		except TypeError:
			print('Неверное значение стоимости или количества, необходимо ввести цифру')
		location = input('Введите расположение товара: ')
		color = input('Введите цвет: ')
		self.item = {'название': name, 'модель': model, 'количество': count,
				'цена': price, 'расположение': location, 'цвет': color}

	def print_tech(self):
		"""Вывести информацию о товаре"""

		print(self.item)

	def edit_location(self):
		"""Изменить информацию о расположении товара"""

		new_location = input('Введите новое расположение товара: ')
		self.item['расположение'] = new_location
	
class Printers(Orgtech):
	def add_tech(self):
		name = input('Введите название: ')
		model = input('Введите модель: ')
		try:
			count = input('Введите количество: ')
			price = input('Введите стоимость: ')
			if not (count.isdigit() == True & price.isdigit() == True):
				raise TypeError
		except TypeError:
			print('Неверное значение стоимости или количества, необходимо ввести цифру')
		location = input('Введите расположение товара: ')
		color = input('Введите цвет: ')
		pr_cartridge = input('Введите объем картриджа: ')
		self.item = {'название': name, 'модель': model, 'количество': count,
					 'цена': price, 'расположение': location, 'цвет': color, 'объем картриджа': pr_cartridge}


class Scanners(Orgtech):
	def add_tech(self):
		name = input('Введите название: ')
		model = input('Введите модель: ')
		try:
			count = input('Введите количество: ')
			price = input('Введите стоимость: ')
			if not (count.isdigit() == True & price.isdigit() == True):
				raise TypeError
		except TypeError:
			print('Неверное значение стоимости или количества, необходимо ввести цифру')
		location = input('Введите расположение товара: ')
		color = input('Введите цвет: ')
		sc_dpi = input('Введите разрешение сканера: ')
		self.item = {'название': name, 'модель': model, 'количество': count,
					 'цена': price, 'расположение': location, 'цвет': color, 'разрешение': sc_dpi}

class Xerox(Orgtech):
	def add_tech(self):
		name = input('Введите название: ')
		model = input('Введите модель: ')
		try:
			count = input('Введите количество: ')
			price = input('Введите стоимость: ')
			if not (count.isdigit() == True & price.isdigit() == True):
				raise TypeError
		except TypeError:
			print('Неверное значение стоимости или количества, необходимо ввести цифру')
		location = input('Введите расположение товара: ')
		color = input('Введите цвет: ')
		xe_speed = input('Введите скорость копирования (кол-во листов в минуту): ')
		self.item = {'название': name, 'модель': model, 'количество': count,
					 'цена': price, 'расположение': location, 'цвет': color, 'скорость копирования': xe_speed}


tech_1 = Orgtech()
tech_1.add_tech()
tech_1.print_tech()
tech_1.edit_location()

pr_1 = Printers()
sc_1 = Scanners()
xe_1 = Xerox()

pr_1.add_tech()
pr_1.print_tech()



