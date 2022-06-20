from exceptions_lesson_11 import IsNumberError
from functions_lesson_11 import number_check

numbers_list = list()

while True:
    number_input = input('Введите число: ')
    if number_input == 'stop' or number_input == '':
        break
    try:
        number_check(number_input)
    except IsNumberError as err:
        print(f"Error: element {err.number} is not of type 'int'")
    else:
        numbers_list.append(number_input)
