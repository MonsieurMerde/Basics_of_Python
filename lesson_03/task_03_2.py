# 2. [Задача со звездочкой]: усложненный вариант задания 1. Написать функцию num_translate_adv,
# которая корректно обработает числительные, начинающиеся с заглавной буквы.
# Если перевод сделать невозможно, вернуть объект None.
# Техническое задание:
# 1. Функция возвращает строку перевод. Или возвращает None, если перевести невозможно.
# 2. Считаем, что только первая буква может быть заглавной.
# 3. Обратите внимание, что функция возвращает перевод в том же регистре, как и приняла.
# 4. Выполнить вызов функции для нескольких слов и вывести на экран результаты.
# Примеры/Тесты:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

dict_numbers = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
                "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}


def num_translate_adv(number_str=None):
    if number_str is not None and number_str.lower() in dict_numbers:
        is_check = number_str.istitle()
        if is_check:
            return dict_numbers[number_str.lower()].title()
        else:
            return dict_numbers[number_str]


print(num_translate_adv('one'))
print(num_translate_adv('Three'))
print(num_translate_adv('eight'))
print(num_translate_adv('Some string'))
print(num_translate_adv())
