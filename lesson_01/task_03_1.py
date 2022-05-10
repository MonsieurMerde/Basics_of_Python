# 3. Реализовать склонение слова "процент" во фразе "N процентов" в интервале от 1 до 101.
# Формат вывода результата:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов
# 101 процент

max_number = 101
number = 1

while number <= max_number:
    number_exception_check = number % 100
    if number % 10 == 0 or 5 <= number % 10 <= 9 or 11 <= number_exception_check <= 14:
        print(f'{number} процентов')
    elif number % 10 == 1:
        print(f'{number} процент')
    else:
        print(f'{number} процента')
    number += 1
