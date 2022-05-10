# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх
# заданных списков.
# Условие задачи:
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Техническое задание:
# 1. Функция должна вернуть список строк-шуток.
# 2. Функция принимает 4 параметра: количество шуток и 3 списка со словами.
# 3. В списках nouns, adverbs, adjectives необязательно одинаковое количество элементов.
# Они могут быть произвольной длины.
# 4. Проверьте работу функции для количества шуток больше, чем длины списков слов и меньше.
# 5. Сделайте вызов функции как с позиционными аргументами, так и с именованными.
# 6. Менять исходные списки nouns, adverbs, adjectives нельзя. Это «side effects»
# 7. Документируйте код функции.
# Примеры/Тесты:
#
# >>> get_jokes(3, nouns, adverbs, adjectives)
# ['автомобиль ночью мягкий', 'лес сегодня утопичный', 'дом вчера зеленый']
# >>> get_jokes(5, nouns, adverbs, adjectives)
# ['автомобиль вчера зеленый',
#  'дом ночью мягкий',
#  'огонь ночью утопичный',
#  'дом позавчера зеленый',
#  'город вчера утопичный']
# >>>

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number_jokes, list1, list2, list3):
    """
    Returns the given number of jokes in list, formed from three random words taken from the three lists of words
    """
    jokes_list = []
    for i in range(number_jokes):
        jokes_list.append(f'{choice(list1)} {choice(list2)} {choice(list3)}')
    return jokes_list


print(get_jokes(2, nouns, adverbs, adjectives))
print(get_jokes(number_jokes=9, list1=nouns, list2=adverbs, list3=adjectives))
