# 2. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield.
# Полностью истощить генератор.
# Техническое задание:
# 1. Все пункты ТЗ задания 1 остаются в силе.
# 2. Отличие от задания 1 - только в использовании yield.

def iterator_with_yield(number):
    for number in range(1, number + 1, 2):
        yield number


n = 25
gen = iterator_with_yield(n)

for n in range(1, n + 3, 2):
    print(next(gen))


