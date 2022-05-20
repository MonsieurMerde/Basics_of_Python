# 1. Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# Техническое задание:
# 1. Не использовать библиотеки для парсинга. Только работа со строками.
# 2. Создать список кортежей вида: '(<remote_addr>, <request_type>, <requested_resource>)'. Именно список кортежей.
# 3. Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# 4. Вывести список на экран.
# Формат вывода результата:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'HEAD', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_1'),
#     ...
# ]

list_tuples = []
with open('nginx_logs.txt', mode='rt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        list_tuples.append((line[0:line.index(' ')],
                            line[line.index('"') + 1:line.index('/downloads/') - 1],
                            line[line.index('/downloads/'):line.index('HTTP') - 1]))

print('[', *list_tuples, ']', sep='\n')
