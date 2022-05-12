# Усложнение [одна звездочка]:
# нужен генератор нечётных чисел от 1 до n (включительно), для чисел, квадрат которых меньше 200.
# Все остальное как в основном задании.

def iterator_without_yield(number):
    number_gen = (number for number in range(1, number + 1, 2) if number ** 2 < 200)
    return number_gen


n = 25
gen = iterator_without_yield(n)

for n in range(1, n + 3, 2):
    print(next(gen), n ** 2)
