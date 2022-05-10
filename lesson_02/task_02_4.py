# 4. Обработка списка чисел.
# Техническое задание:

# 1. Создать список, содержащий цены на товары (10–20 товаров), например: [57.8, 46.51, 97, ...].
# 2. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Обратите внимание на изменение формата вывода.

list_numbers = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12]
list_numbers_string = []
for number in list_numbers:
    number_string = str(number)
    if '.' in number_string:
        rub, pennies = number_string.split('.')
        if len(pennies) == 1:
            pennies = f'0{pennies}'
        number_string = f'{rub} руб {pennies} коп,'
    else:
        number_string = f'{number_string} руб 00 коп,'
    list_numbers_string.append(number_string)

string_numbers = ' '.join(list_numbers_string)

print('Исходный список:')
print(list_numbers)
print(string_numbers)

# 3. Вывести на экран цены (как числа), отсортированные по возрастанию,
# новый список для этого не создавать (показать, что объект списка после сортировки остался тот же).

print('Доказательство операции in place:')
print(f'id перед сортировкой: {id(list_numbers)}')
list_numbers.sort()
print(f'id после сортировки: {id(list_numbers)}')
print(list_numbers)

# 4. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Показать, что это другой список, другой объект.

# Сделал 2 варианта. Честно говоря, не знаю, в чём между ними разница, скорее всего, что-то неправильно понимаю в
# работе Python.

list_numbers_descending = list(reversed(list_numbers))
print(f'id перед сортировкой: {id(list_numbers)}')
print(f'id после сортировки: {id(list_numbers_descending)}')
print(list_numbers_descending)

list_numbers_copy = list_numbers.copy()
list_numbers_descending_v2 = list(reversed(list_numbers_copy))
print(f'id перед сортировкой: {id(list_numbers)}')
print(f'id после сортировки: {id(list_numbers_descending_v2)}')
print(list_numbers_descending_v2)

# 5. Вывести цены пяти самых дорогих товаров.
print('5 самых дорогих товаров:')
for i in range(5):
    print(list_numbers_descending[i])
