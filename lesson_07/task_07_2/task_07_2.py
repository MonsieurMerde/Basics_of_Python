import os
from functions import line_cleaning, make_file

with open('config_2.yaml', mode='r', encoding='utf-8') as file_yaml:
    double_space_count_prev = 0
    path = os.path.abspath('task_07_2.py')
    for line in file_yaml:
        double_space_count_current = line.count('  ')
        line = line.strip()
        clear_name = line_cleaning(line)
        if double_space_count_current == double_space_count_prev:
            # Здесь специально не стал загонять os.path.join(...) в os.path.dirname(...), показалось, что для восприятия так лучше.
            path = os.path.dirname(path)
            path = os.path.join(path, clear_name)
            make_file(line, path)
        elif double_space_count_current > double_space_count_prev:
            path = os.path.join(path, clear_name)
            make_file(line, path)
        else:
            for _ in range(double_space_count_prev - double_space_count_current + 1):
                path = os.path.dirname(path)
            path = os.path.join(path, clear_name)
            make_file(line, path)
        double_space_count_prev = double_space_count_current

# Не уверен, что с точки зрения философии Питона сделал правильно.
# Может быть, лучше всё-таки было не выводить функцией сообщения о том, что файлы/папки были созданы, а обрабатывать ошибки?
