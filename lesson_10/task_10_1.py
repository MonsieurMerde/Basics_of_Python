class Matrix:

    def __init__(self, matrix):
        for string in matrix:
            if len(matrix[0]) != len(string):
                raise ValueError('Incorrect data for Matrix initialization: not equal length of strings')
            for elem in string:
                if type(elem) != int:
                    raise ValueError('Incorrect data for Matrix initialization: type of one of the Matrix elements not int')
        self.matrix = matrix
        self.strings_count = len(matrix)
        self.columns_count = len(matrix[0])

    def __str__(self):
        matrix_str = ''
        for string in self.matrix:
            matrix_str += '|'
            for elem in string:
                matrix_str += f'{elem:>5}'
            matrix_str += ' |'
            if string != self.matrix[-1]:
                matrix_str += '\n'
        return matrix_str

    def __add__(self, other_matrix):
        if type(other_matrix) != Matrix:
            raise TypeError('Second object is not a Matrix')
        if self.strings_count != other_matrix.strings_count or self.columns_count != other_matrix.columns_count:
            raise ValueError('Incorrect dimensions for add method')
        else:
            matrix_sum = [
                [elem_1 + elem_2 for elem_1, elem_2 in zip(string_matrix, string_other_matrix)]
                for string_matrix, string_other_matrix in zip(self.matrix, other_matrix.matrix)
            ]
        return Matrix(matrix_sum)


m_1 = Matrix([[11, 5, 3], [4, 5, 6], [117, 8, -118]])
m_2 = Matrix([[25, 44, 12], [5, 42, 33], [12, -77, -3]])
print(m_1)
print(type(m_1))
print(m_2)
print(type(m_2))
m_3 = m_1 + m_2
print(m_3)
print(type(m_3))
m_4 = Matrix([[4, 22, 10, 5], [-35, 4, -7, 11], [-36, 11, 45, 14]])
print(m_4)
print(type(m_4))
