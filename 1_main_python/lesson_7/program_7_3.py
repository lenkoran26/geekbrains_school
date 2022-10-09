#Task_7_3

class Cell():
	
	def __init__(self, n):
		self.count_cells = n

	def __add__(self, other):
		return self.count_cells + other.count_cells

	def __sub__(self, other):
		if self.count_cells > other.count_cells:
			return self.count_cells - other.count_cells
		else:
			return "Negative result"

	def __mul__(self, other):
		return self.count_cells * other.count_cells

	def __truediv__(self, other):
		return round(self.count_cells // other.count_cells)

	def make_order (self, k):
		count_lines = self.count_cells // int(k)
		reminder = self.count_cells % int(k)
		lines = ""
		for i in range(count_lines):
			lines += '*' * int(k)
			lines += '\n'
		lines += '*' * reminder
		return lines

cell_1 = Cell(13)
cell_2 = Cell(5)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
