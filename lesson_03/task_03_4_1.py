# 4. [Задача со звездочкой]: усложненный вариант задания 3. Написать функцию thesaurus_adv(), принимающую в качестве
# аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается
# с соответствующей буквы.
# Техническое задание:
# 1. Количество передаваемых строк в функцию может быть любым. Считаем, что переданы будут только корректные строки.
# 2. Вернуть словарь, с ключами, отсортированными в алфавитном порядке.
# Примеры/Тесты:
# >>> thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
#            "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков")
# {
#    'А':{
#           'П': ['Петр Алексеев']},
#    'И': {
#           'И': ['Илья Иванов']},
#    'С': {
#           'А': ['Алла Сидорова', 'Анна Савельева'],
#           'В': ['Василий Суриков'],
#           'И': ['Иван Сергеев', 'Инна Серова']}}

peoples = ("Иван Сергеев", "Алла Сидорова", "Инна Серова", "Петр Алексеев",
           "Илья Иванов", "Анна Савельева", "Василий Суриков")


def thesaurus_adv(*args):
    big_dict = {}
    for people in args:
        name, surname = people.split(' ')
        if surname[0] not in big_dict:
            big_dict.setdefault(surname[0], {name[0]: [people]})
        else:
            if name[0] in big_dict[surname[0]]:
                big_dict[surname[0]][name[0]].append(people)
            else:
                big_dict[surname[0]].setdefault(name[0], [people])

    for letter_surname in big_dict:
        big_dict[letter_surname] = dict(sorted(big_dict[letter_surname].items()))
    big_dict = dict(sorted(big_dict.items()))
    return big_dict


print('{')
for key1, value1 in thesaurus_adv(*peoples).items():
    print(f"\t'{key1}':" "{")
    for key2, value2 in value1.items():
        print(f"\t\t'{key2}': {value2}")
    print('\t\t}')
print('}')
