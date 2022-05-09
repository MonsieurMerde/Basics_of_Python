from utils import currency_rates, currency_rates_advanced

url = 'http://www.cbr.ru/scripts/XML_daily.asp'

print(currency_rates(url, 'HKD'))
print(currency_rates(url, 'iNr'))
print(currency_rates(url, 'ABC'))
print(currency_rates(url))
print(currency_rates_advanced(url, 'nok'))
print(currency_rates_advanced(url, 'AUD'))
print(currency_rates_advanced(url, 'xhu'))
print(currency_rates_advanced(url))
