# 6. [Задача со звездочкой]: усложненный вариант задания 5.
# Техническое задание:
# 1. Добавьте в функцию еще один аргумент, разрешающий или запрещающий повторы слов в шутках:
# каждое слово можно использовать только в одной шутке. Тогда этот параметр логично сделать типом boolean.
# 2. Функция должна вернуть список строк-шуток сколько потребовали или сколько получилось из условия уникальности.
# 3. Проверьте работу функции для разного количества шуток. Убедитесь в том, что каждое слово встречается
# только один раз.

import random
from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number_jokes, list1, list2, list3, is_repeat):
    jokes_list = []
    if is_repeat:
        for i in range(number_jokes):
            jokes_list.append(f'{choice(list1)} {choice(list2)} {choice(list3)}')
    else:
        number_jokes = min(number_jokes, min(len(list1), len(list2), len(list3)))
        for word1, word2, word3 in zip(random.sample(list1, number_jokes), (random.sample(list2, number_jokes)),
                                       (random.sample(list3, number_jokes))):
            jokes_list.append(f'{word1} {word2} {word3}')
    return jokes_list


print(get_jokes(10, nouns, adverbs, adjectives, True))
print(get_jokes(3, nouns, adverbs, adjectives, True))
print(get_jokes(8, nouns, adverbs, adjectives, False))
