# Усложнение [одна звездочка]:
# С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно), для чисел,
# квадрат которых меньше 200.


def iterator_with_yield(number):
    for number in range(1, number + 1, 2):
        if number ** 2 < 200:
            yield number


n = 25
gen = iterator_with_yield(n)

for n in range(1, n + 3, 2):
    print(next(gen))
