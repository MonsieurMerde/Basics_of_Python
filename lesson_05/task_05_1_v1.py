# 1. Написать генератор нечётных чисел от 1 до n (включительно), без использования ключевого слова yield,
# полностью истощить генератор.
# Формат вывода результата:
# 1. Программа явно должна закончиться на StopIteration
# Техническое задание:
# 1. n - любое положительное число.
# 2. Создание генератора сделайте внутри функции iterator_without_yield(n),
# принимающей аргументом n любое положительное число и возвращающей генератор.
# 3. Не путайте истощение генератора и печать его значений. Выполнение программы должно закончиться
# на исключении StopIteration. Истощение генератора - любым удобным для вас способом.
# Примеры/Тесты:
# gen1 = iterator_without_yield(11)
# next(gen1)
# 1
# next(gen1)
# 3
# next(gen1)
# 5
# next(gen1)
# 7
# next(gen1)
# 9
# next(gen1)
# 11
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration


def iterator_without_yield(number):
    number_gen = (number for number in range(1, number + 1, 2))
    return number_gen


n = 16
gen = iterator_without_yield(n)

for n in range(1, n + 3, 2):
    print(next(gen))
