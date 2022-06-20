from exceptions_lesson_11 import MyZeroDivisionError
from functions_lesson_11 import division

# Насколько правильно выносить исключения в отдельный модуль?


numbers_list = [(1, 3), (2, 4), (56, -22), (11, 0)]

for numbers in numbers_list:
    number_1, number_2 = numbers
    try:
        print(division(number_1, number_2))
    except MyZeroDivisionError as err:
        print(f"Error: can't divide {err.number_1} to {err.number_2}")
