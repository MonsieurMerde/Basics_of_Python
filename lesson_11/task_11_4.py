from functions_lesson_11 import output_complex_number


class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return output_complex_number(self.x, self.y)

    def __add__(self, other_number):
        return Complex(self.x + other_number.x, self.y + other_number.y)

    def __sub__(self, other_number):
        return Complex(self.x - other_number.x, self.y - other_number.y)

    def __mul__(self, other_number):
        return Complex(self.x * other_number.x - self.y * other_number.y, self.y * other_number.x + self.x * other_number.y)


c_1 = Complex(5, 6)
print(c_1, type(c_1))
c_2 = Complex(2, -3)
c_3 = c_1 + c_2
print(c_3, type(c_3))
c_4 = c_2 - c_3
print(c_4, type(c_4))
c_5 = c_4 * c_2
print(c_5, type(c_5))
