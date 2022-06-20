from datetime import datetime
from exceptions_lesson_11 import DateInitError


class Date:

    @classmethod
    def extraction(cls, date_str):
        try:
            day, month, year = date_str.split('-')
            return int(day), int(month), int(year)
        except (AttributeError, ValueError):
            raise ValueError

    @staticmethod
    def is_validation_date(date_tuple):
        day, month, year = date_tuple
        try:
            datetime(year, month, day)
        except ValueError:
            return False
        else:
            return True

    def __init__(self, date_str):
        try:
            Date.extraction(date_str)
        except ValueError:
            raise DateInitError(f"{date_str}: error in date input format: enter date in the format 'day-month-year' (type 'string')")
        if Date.is_validation_date(Date.extraction(date_str)):
            self.date_str = date_str
        else:
            raise DateInitError(f"{date_str}: invalid range for days, month, or year")

    def __str__(self):
        day, month, year = self.date_str.split('-')
        return f'{year}-{month}-{day}'


dates_list = ['31-12-2021', '32-12-2033', '12-12--2022', '29-02-2019', '29-02-2020', 2022, '12-2022']
for date in dates_list:
    try:
        print(Date(date))
    except DateInitError as e:
        print(e)
