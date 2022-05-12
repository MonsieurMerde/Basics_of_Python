# Усложнение [две звездочки]:
# С ключевым словом yield: Вычислять и возвращать само число и накопительную сумму этого и предыдущих чисел.
# Например:
# gen1 = iterator_with_yield(14)
# next(gen1)
# (1, 1)
# next(gen1)
# (3, 4)
# next(gen1)
# (5, 9)
# next(gen1)
# (7, 16)
# next(gen1)
# (9, 25)
# next(gen1)
# (11, 36)
# next(gen1)
# (13, 49)
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration


def iterator_with_yield(number):
    number_sum = 0
    for number in range(1, number + 1, 2):
        if number ** 2 < 200:
            number_sum += number
            yield number, number_sum


n = 8
gen = iterator_with_yield(n)

for n in range(1, n + 3, 2):
    print(next(gen))
