from datetime import date
from requests import get, utils


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


def currency_rates_advanced(url, currency=None):
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    if currency is not None and currency.upper() in content:
        value = currency_rates(url, currency)
        date_index = content.index('Date=')
        day, month, year = content[date_index + 6: date_index + 16].split('.')
        date_datetime = date(int(year), int(month), int(day))
        return date_datetime, value


# Комментарий по поводу вызова из функции currency_rates_advanced уже написанной функции currency_rates:
# Плюсы: придерживаемся принципа DRY.
# Минусы: если currency_rates и currency_rates_advanced будут находиться в разных модулях, при использовании функции
# currency_rates_advanced нужно будет дополнительно импортировать currency_rates.
