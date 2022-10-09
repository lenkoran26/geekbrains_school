#Task_7_1

class Matrix:
    _new_mat = list()
    count = 0
    def __init__(self, list):
        self.list = list
        Matrix.count += 1
        print(f'{self.count} - я матрица:')
    def __str__(self):
        matrix = self.list
        s = ''
        for i in matrix:
            s += str(i) + '\n'
        return s

    def __add__(self, other):
        matrix = self.list
        line = list()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                line.insert(j, int(self.list[i][j]) + int(other.list[i][j]))
                line_to_matrix = line.copy()
            self._new_mat.insert(i, line_to_matrix)
            line.clear()

        return Matrix(self._new_mat)

a = Matrix([[1,1,1],[2,2,2],[3,3,3]])
print(a)
b = Matrix([[4,4,4],[1,1,1],[2,2,2]])
print(b)
print(a + b)