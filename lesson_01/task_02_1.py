# 2. Для кубов нечётных чисел от 1 до 1000 вычислить сумму чисел, сумма цифр кубов которых делится нацело на 7.
# Вывод на экран формить в виде: число ^3 = куб_числа; [сумма цифр куба] накопительная_сумма
# Например:
# 19 ^3 = 6859 [ 28 ] накоп. сумма: 19
# 31 ^3 = 29791 [ 28 ] накоп. сумма: 50
# ...
# 967 ^3 = 904231063 [ 28 ] накоп. сумма: 43106

max_number = 1000
number = 1
cumulative_sum = 0

while number <= max_number:
    number_sum = 0
    number_cube = number ** 3
    while number_cube:
        number_sum += number_cube % 10
        number_cube //= 10
    if not number_sum % 7:
        cumulative_sum += number
        print(f'{number} ^3 = {number ** 3} [{number_sum}]; накоп. сумма: {cumulative_sum}')
    number += 2
