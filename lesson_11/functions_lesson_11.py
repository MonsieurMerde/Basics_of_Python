from exceptions_lesson_11 import IsNumberError, MyZeroDivisionError


def division(number_1, number_2):
    try:
        number_1 / number_2
    except ZeroDivisionError:
        raise MyZeroDivisionError(number_1, number_2)
    else:
        return number_1 / number_2


def number_check(elem):
    try:
        elem = int(elem)
    except ValueError:
        raise IsNumberError(elem)
    else:
        return elem


def output_complex_number(a, b):
    if b == 0:
        return f'{a}'
    elif b > 0:
        return f'{a}+{b}j'
    elif a == 0:
        if b == -1:
            return '-j'
        elif b == 1:
            return 'j'
        else:
            return f'{b}j'
    else:
        return f'{a}{b}j'
