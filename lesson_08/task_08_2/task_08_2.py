from functions import log_parse

with open('nginx_logs.txt', mode='r', encoding='utf-8') as file:
    ip_list = []
    for line in file:
        if log_parse(line)[0][0] not in ip_list:
            ip_list.append(log_parse(line)[0][0])

print(len(ip_list))
