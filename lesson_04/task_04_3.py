# 3. [Задача со звездочкой]: усложненный вариант задания 2.
# Доработать функцию currency_rates: теперь она должна возвращать курс валюты и дату, которая передаётся
# в ответе сервера. Название новой функции currency_rates_advanced.
# Техническое задание:
# 1. Все требования задания 2 остаются в силе.
# 2. Функция должна вернуть список или кортеж, содержащий дату и курс валюты.
# 3. Дата должна быть объектом date пакета datetime стандартной библиотеки.
# Для ее создания используйте функции пакета datetime. Если это слишком сложно - оставьте дату строкой.
# Формат вывода результата:
# 1. Вызовите функцию для нескольких валют, обязательно для несуществующей валюты,
# продемонстрируйте правильность работы.
# Примеры/Тесты:
# >>> url = "<http://www.cbr.ru/scripts/XML_daily.asp>"
# >>> currency_rates_advanced(url, "USd")
# ([datetime.date(2021, 10, 15)], 71.7846)
# >>> currency_rates_advanced(url, "EuR")
# ([datetime.date(2021, 10, 15)], 83.3347)
# >>> currency_rates_advanced(url, "GBP")
# ([datetime.date(2021, 10, 15)], 98.3449)
# >>> currency_rates_advanced(url, "GBP2")
# ([datetime.date(2021, 10, 15)], None)

from datetime import date
from requests import get, utils

url_address = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates_advanced(url, currency=None):
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    if currency is not None and currency.upper() in content:
        currency = currency.upper()
        currency_index = content.index(currency)
        value = float(content[content.index('<Value>', currency_index) + 7:
                              content.index('</Value>', currency_index)].replace(',', '.'))
        date_index = content.index('Date=')
        day, month, year = content[date_index + 6: date_index + 16].split('.')
        data = date(int(year), int(month), int(day))
        return data, value


print(currency_rates_advanced(url_address, 'CNY'))
print(currency_rates_advanced(url_address, 'xdr'))
print(currency_rates_advanced(url_address, 'uAh'))
print(currency_rates_advanced(url_address, 'YYY'))
print(currency_rates_advanced(url_address))
