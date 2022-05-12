# 5. Задан список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке.
# Техническое задание:
# 1. Здесь нет условия создавать итератор/генератор или comprehensions.
# 2. Сохранение исходного порядка в результирующем списке обязательно.
# 3. Не используйте Counter из модуля collections или аналогичные.
# Примеры/Тесты:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_numbers_set = set()
temp_set = set()

for elem in src:
    unique_numbers_set.discard(elem) if elem in temp_set else unique_numbers_set.add(elem)
    temp_set.add(elem)

result = [number for number in src if number in unique_numbers_set]

print(src)
print(result)
