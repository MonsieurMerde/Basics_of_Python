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


def log_parse(log_raw):
    data_log = re.compile(r'''(^[\d.]+|^[0-9A-Fa-f:]{2,39}) # remote_addr
                              \s-\s-\s\[
                              (\d{2}/[A-Za-z]+/\d{4}:\d{2}:\d{2}:\d{2}\s\+[0]{4}) # request_datetime
                              ]
                              \s
                              "
                              (\w+) # request_type
                              \s
                              ([\w/]+) # requested_resource
                              \s
                              [A-Za-z/\d{1}.]+
                              "
                              \s
                              (\d+) # response_code
                              \s
                              (\d+) # response_size
                               ''', re.VERBOSE)
    return data_log.findall(log_raw)