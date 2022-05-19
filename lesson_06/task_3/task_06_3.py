# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Загрузить данные из обоих файлов и
# сформировать словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в текстовый файл. Проверить сохранённые данные.
# Техническое задание:
# 1. Данные файлов синхронизированы построчно: 1-ой строке файла с ФИО соответствует 1-ая строка файла с хобби и т.п.
# 2. При хранении данных используется принцип: одна строка — один пользователь.
# 3. Разделитель между значениями — запятая. Не используем пакеты для парсинга CSV файлов.
# При формировании словаря - хобби следует разделить символом «точка с запятой».
# 4. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, то для оставшихся ФИО использовать вместо хобби None.
# 5. Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1».
# 6. При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# 7. Вы можете использовать здесь функции zip и zip_longest, но лучше обойтись без них.
# Примеры/Тесты:
# Фрагмент файла с данными о пользователях (task_3_users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Сидоров,Сидор,Сидорович
# Фрагмент файла с данными о хобби (task_3_hobby.csv):
# скалолазание,охота
# горные лыжи
# вышивание крестиком,бои без правил
# Фрагмент результирующего файла (task_3_rezult.txt):
# {'ИИИ': 'скалолазание;охота', 'ППП': 'горные лыжи', 'ССС': 'вышивание крестиком;бои без правил'}

import json

with open('task_3_users.csv', mode='r', encoding='utf-8-sig') as f:
    users_list = f.read().strip().splitlines()

with open('task_3_hobby.csv', mode='r', encoding='utf-8-sig') as f:
    hobby_list = f.read().strip().splitlines()


def abbreviation_user(user):
    abbreviation = ''
    for letter in user:
        if letter.istitle():
            abbreviation += letter
    return abbreviation


users_and_hobby_dict = {}

for i in range(max(len(users_list), len(hobby_list))):
    if i >= len(users_list):
        exit(1)
    elif i >= len(hobby_list):
        users_and_hobby_dict.setdefault(abbreviation_user(users_list[i]), None)
    else:
        users_and_hobby_dict.setdefault(abbreviation_user(users_list[i]), hobby_list[i].replace(',', ';'))

with open('task_3_rezult.txt', mode='w', encoding='utf-8') as f:
    f.write(str(users_and_hobby_dict))

with open('task_3_rezult.json', mode='w', encoding='utf-8') as f:
    json.dump(users_and_hobby_dict, f, ensure_ascii=False)
