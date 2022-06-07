import re


def email_parse(email_address):
    data_email_domain = re.compile(r'''(?P<username>^[a-zA-Z\d'._+-]+?)
                                       @
                                       (?P<domain>[a-zA-Z_.-]*\.[a-zA-Z]{2})
                                       ''', re.VERBOSE)
    try:
        data_email_domain.search(email_address).groupdict()
    except AttributeError:
        raise ValueError
    else:
        return data_email_domain.search(email_address).groupdict()


with open('task_8_1_test_email.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        try:
            print(line[:line.find(' ')], '', email_parse(line))
        except ValueError:
            print(line[:line.find(' ')], '', 'Error')
