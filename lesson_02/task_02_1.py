# 1. Выяснить тип результата следующих выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2
# Техническое задание:
# Вывести на экран тип выражения и отдельно проверить является ли полученный тип целым числом.

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

print(isinstance(15 * 3, int))
print(isinstance(15 / 3, int))
print(isinstance(15 // 2, int))
print(isinstance(15 ** 2, int))
