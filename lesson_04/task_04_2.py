# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю.
# Техническое задание:
# 1. Использовать библиотеку requests. В качестве API использовать http://www.cbr.ru/scripts/XML_daily.asp.
# 2. Функция currency_rates принимает два аргумента: строка с URL, куда стучимся и строку с кодом валюты (только одной).
# Возвращает результат числового типа, например float. Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть объект None.
# 3. Для извлечения данных использовать только методы объект str.
# 4. Сделать работу функции не зависящей от того, в каком регистре был передан код валюты.
# 5. Функция должна корректно обрабатывать любой код валюты. Правильность параметра url можно не проверять.
# 6. Вводить коды валют с клавиатуры (input) необязательно.
# Формат вывода результата:
# 1. Вызовите функцию для нескольких валют, обязательно для несуществующей валюты,
# продемонстрируйте правильность работы.
# Примеры/Тесты:
# >>> url = "<http://www.cbr.ru/scripts/XML_daily.asp>"
# >>> currency_rates(url, "USd")
# 71.7846
# >>> currency_rates(url, "EuR")
# 83.3347
# >>> currency_rates(url, "GBP")
# 98.3449
# >>> currency_rates(url, "GBP2")
# >>>


from requests import get, utils

url_address = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(url, currency=None):
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    if currency is not None and currency.upper() in content:
        currency = currency.upper()
        currency_index = content.index(currency)
        value = float(content[content.index('<Value>', currency_index) + 7:
                              content.index('</Value>', currency_index)].replace(',', '.'))
        return value


print(currency_rates(url_address, 'Usd'))
print(currency_rates(url_address, 'kgS'))
print(currency_rates(url_address, 'ZAR'))
print(currency_rates(url_address, 'XXX'))
print(currency_rates(url_address))
