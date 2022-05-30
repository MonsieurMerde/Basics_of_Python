import os


def line_cleaning(line_string):
    if line_string.find('- ') != -1:
        line_string = line_string[line_string.index('- ') + 2:]
    if line_string.endswith(':'):
        line_string = line_string[:-1]
    return line_string


def make_file(line_string, path_file):
    clean_name = line_cleaning(line_string)
    directory = os.path.dirname(path_file)
    if os.path.exists(path_file):
        if line_string.endswith(':'):
            print(f'Папка {clean_name} в директории {directory} уже существует.')
        else:
            print(f'Файл {clean_name} в директории {directory} уже существует.')
    else:
        if line_string.endswith(':'):
            os.mkdir(path_file)
        else:
            f = open(path_file, mode='a', encoding='utf-8')
            f.close()


def dict_creation(lower_value, upper_value, multiplicity, is_advanced=False):
    dictionary = {}
    while lower_value <= upper_value:
        if not is_advanced:
            dictionary.setdefault(lower_value, 0)
        else:
            dictionary.setdefault(lower_value, [0, []])
        lower_value *= multiplicity
    return dictionary
