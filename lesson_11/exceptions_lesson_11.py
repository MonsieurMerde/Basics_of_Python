class DateInitError(Exception):
    def __init__(self, message):
        self.message = message


class IsNumberError(Exception):
    def __init__(self, number):
        self.number = number


class MyZeroDivisionError(Exception):
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
