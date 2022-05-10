list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2 = ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5',
          'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
list_3 = ['+9', 'примерно в', '23', 'часа', '8', 'минут', '03', '05', 'секунд', 'температура', 'воздуха', 'была',
          '5', 'градусов Цельсия', 'темп', 'воды', '+2.0', 'градусов', 'Цельсия', '-2', '11']

for idx_lst, lst in enumerate([list_1, list_2, list_3]):
    print(f'{idx_lst}. Исходный список:', lst)
    new_list = []

    for element in lst:
        if element[0] == '-' or element[0] == '+':
            if element[1:].isdigit():
                if len(element[1:]) == 1:
                    new_list.extend(['"', f'{element[0]}0{element[1:]}', '"'])
                else:
                    new_list.extend(['"', element, '"'])
            else:
                new_list.append(element)
        elif element.isdigit():
            if len(element) == 1:
                new_list.extend(['"', f'0{element}', '"'])
            else:
                new_list.extend(['"', element, '"'])
        else:
            new_list.append(element)

    print('    0. Новый список + добавление элементов-кавычек:', new_list)
    new_string = ''

# Первый вариант формирования строки из нового списка:
    for idx, elem in enumerate(new_list):
        if idx == len(new_list) - 1:
            new_string += f'{elem}'
        else:
            if elem == '"':
                if ((new_list[idx + 1][0] == '+' or new_list[idx + 1][0] == '-') and new_list[idx + 1][1:].isdigit())\
                        or new_list[idx + 1].isdigit():
                    new_string += f'{elem}'
                else:
                    new_string += f'{elem} '
            elif ((elem[0] == '+' or elem[0] == '-') and elem[1:].isdigit()) or elem.isdigit():
                new_string += f'{elem}'
            else:
                new_string += f'{elem} '

    print('    1. Окончательная строка:', new_string)

# Второй вариант формирования строки из нового списка.
# Когда придумал решение усложнённой задачи 2, подумал о том, что подобный алгоритм можно применить и здесь.
# Чтобы его продемонстрировать, не стал заново делать новый список из исходных, а сразу взял списки с добавленными
# элементами-кавычками. Какой из них лучше? :)

print('\nВторой вариант формирования строки из нового списка:\n')

new_list_1_v2 = ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05',
                 '"', 'градусов']
new_list_2_v2 = ['примерно в', '"', '23', '"', 'часа', '"', '08', '"', 'минут', '"', '03', '"', 'секунд', 'температура',
                 'воздуха', 'была', '"', '-05', '"', 'градусов Цельсия', 'темп', 'воды', '"', '+12', '"', 'градусов',
                 'Цельсия']
new_list_3_v2 = ['"', '+09', '"', 'примерно в', '"', '23', '"', 'часа', '"', '08', '"', 'минут', '"', '03', '"', '"',
                 '05', '"', 'секунд', 'температура', 'воздуха', 'была', '"', '05', '"', 'градусов Цельсия', 'темп',
                 'воды', '+2.0', 'градусов', 'Цельсия', '"', '-02', '"', '"', '11', '"']

for new_list_v2 in [new_list_1_v2, new_list_2_v2, new_list_3_v2]:
    print('0. Новый список + добавление элементов-кавычек:', new_list_v2)
    string_v2 = ''
    i = 0
    while i <= len(new_list_v2) - 1:
        if i == len(new_list_v2) - 1:
            string_v2 += new_list_v2[i]
            i += 1
        elif new_list_v2[i] == '"':
            if i + 2 == len(new_list_v2) - 1:
                string_v2 += f'{new_list_v2[i]}{new_list_v2[i + 1]}{new_list_v2[i + 2]}'
                i += 3
            else:
                string_v2 += f'{new_list_v2[i]}{new_list_v2[i + 1]}{new_list_v2[i + 2]} '
                i += 3
        else:
            string_v2 += f'{new_list_v2[i]} '
            i += 1

    print('1. Окончательная строка:', string_v2)
