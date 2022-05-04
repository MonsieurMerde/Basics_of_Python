# 1. Написать функцию num_translate, переводящую числительные от 0 до 10 с английского на русский язык.
# Техническое задание:
# 1. Функция num_translate возвращает строку перевод. Или возвращает None, если перевести невозможно.
# Обратите внимание, что возвращается None как объект, а не как строка "None".
# Не путайте печать значения (print) и его возврат из функции (return).
# 2. Функция принимает параметр - строку слово для перевода, и другие параметры, если нужно - по вашему усмотрению.
# В примере специально они не указаны.
# 3. Здесь нет требований на регистр входного слова. Возвращается результат в нижнем регистре.
# 4. Выполнить вызов функции для нескольких слов и вывести на экран результаты.
# Примеры/Тесты:
#
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

dict_numbers = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
                "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}


def num_translate(number_str=None):
    if number_str is not None and number_str.lower() in dict_numbers:
        return dict_numbers[number_str.lower()]


print(num_translate('one'))
print(num_translate('Two'))
print(num_translate('fOuR'))
print(num_translate('Some string'))
print(num_translate())
