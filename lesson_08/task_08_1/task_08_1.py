from functions import email_parse

with open('task_8_1_test_email.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        try:
            print(line[:line.find(' ')], '', email_parse(line))
        except ValueError:
            print(line[:line.find(' ')], '', 'Error')
