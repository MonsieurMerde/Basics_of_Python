# 5. [Задача со звездочкой]: усложненный вариант задания 4. Добавить возможность редактирования данных при помощи отдельного скрипта.
# Техническое задание:
# 1. Скрипт получает два параметра: номер записи и новое значение
# 2. Файл не должен считываться в память целиком. Обязательно.
# 3. Не создавать дополнительных/«промежуточных» файлов
# 4. Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует: ничего в файле не меняем, выводим сообщение в консоль.


from sys import argv
from itertools import islice

if len(argv) == 1 or len(argv) == 2:
    print('Введите 2 параметра: номер записи и новое значение.')
elif len(argv) > 3:
    print('Вы ввели больше двух значений.')
elif argv[1] == '0' or not argv[1].isdigit() or not argv[2].isdigit():
    print('Вы ввели номер записи, который не существует, или неверное значение.')
elif len(argv) == 3:
    number_line = int(argv[1])
    new_value = argv[2]
    position = 1
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        start_cursor = f.tell()
        remainder_list = list(islice(f, number_line, None))
        f.seek(start_cursor)
        if len(remainder_list) == 0:
            print('Вы ввели номер записи, который не существует.')
        else:
            if number_line == 1:
                f.seek(f.tell())
                f.write(new_value + '\n')
            else:
                line = f.readline()
                while line:
                    if position == number_line - 1:
                        f.seek(f.tell())
                        f.write(new_value + '\n')
                        break
                    position += 1
                    line = f.readline()
            for ln in remainder_list:
                f.write(ln)
            f.truncate()
