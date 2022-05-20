# 2. [Задача со звездочкой]: усложненный вариант задания 1. Найти IP адрес спамера и количество отправленных им запросов
# по данным файла логов из предыдущего задания. Спамер — это клиент, отправивший больше всех запросов.
# Формат вывода результата:
# 1. Вывести IP спамера и количество запросов от него.
# Техническое задание:
# 1. Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# 2. У нас изначально нет никакой информации о максимальном количестве запросов. Его надо определить из лог-файла.
# 3. Не используйте сторонние модули для подсчетов, типа «count» - они вам не нужны.
# 4. Не используйте затратные операций типа сортировки и поисков. Они здесь абсолютно избыточны.
# Для примера представьте, что более половина лог-файла - это запросы от спамера.
# Оцените эффективность вашего алгоритма в таком случае.

nginx_logs_dict = {}
with open('nginx_logs.txt', mode='rt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        ip_address = line[0:line.index(' ')]
        if ip_address in nginx_logs_dict:
            nginx_logs_dict[ip_address] += 1
        else:
            nginx_logs_dict.setdefault(ip_address, 1)

# Часть кода выше с блоком if-else не работает в виде тернарного оператора:
# nginx_logs_dict[ip_address] += 1 if ip_address in nginx_logs_dict else nginx_logs_dict.setdefault(ip_address, 1)
# Работает только так:
# nginx_logs_dict[ip_address] = nginx_logs_dict[ip_address] + 1 if ip_address in nginx_logs_dict else nginx_logs_dict.setdefault(ip_address, 1)
# Какой вариант с точки зрения философии Питона лучше? Который я оставил или всё-таки в виде тернарного оператора?

max_value = max(nginx_logs_dict.values())
spammers_list = [key for key in nginx_logs_dict if nginx_logs_dict[key] == max_value]
print('Спамер(ы):')
for spammer in spammers_list:
    print(f'IP спамера: {spammer}, количество запросов: {max_value}')
