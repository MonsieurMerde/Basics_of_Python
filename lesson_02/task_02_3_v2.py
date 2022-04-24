# 3. Дан список, содержащий искаженные данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита'].
# Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
# Техническое задание:
# 1. Список может содержать произвольное количество элементов.
# 2. Имя сотрудника - всегда последнее слова в строке. Может содержать заглавные или строчные буквы в любом порядке.
# 3. В результате имя сотрудника пишется строчными буквами и первая буква - заглавная.
# Формат вывода результата:
# Усложнение:
# Выполните условие задачи, но формат вывода включает и должность, например:
# Привет, инженер-конструктор Игорь!
# Привет, главный бухгалтер Марина!
# ...

employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for employee in employees:
    index_last_space = 0
    for index, element in enumerate(employee):
        if element == ' ':
            index_last_space = index
    print(f'Привет, {employee[:index_last_space]}{employee[index_last_space:].upper().title()}!')
