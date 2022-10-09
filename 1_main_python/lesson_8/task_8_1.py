#Task_8_1

class Date():
	
	def __init__(self, day, month, year):
		self.d = day
		self.m = month
		self.y = year
		
	@classmethod
	def convert(cls, d_m_y):
		dmy = list()
		dmy = d_m_y.split('-')
			
		return cls(int(dmy[0]), int(dmy[1]), int(dmy[2]))

	@staticmethod
	def check(d,m,y):
		error_date = ''
		if not(1 <= d <= 31):
			error_date += 'Fail day '
		if not(1 <= m <= 12):
			error_date += 'Fail month '
		if not(1 <= y <= 2021):
			error_date += 'Fail year'

		if error_date == '':
			return f'OK'
		else:
			return error_date


date_1 = Date.convert('32-13-2020')

print (f'day {date_1.d} - type {type(date_1.d)}')
print (f'month {date_1.m} - type {type(date_1.m)}')
print (f'year {date_1.y} - type {type(date_1.y)}')

print(date_1.check(date_1.d, date_1.m, date_1.y))