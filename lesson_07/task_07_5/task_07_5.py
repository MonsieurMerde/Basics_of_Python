import json
import os
from functions import dict_creation

path_some_data = os.path.abspath('some_data_adv')
some_data_files_sizes_adv = dict_creation(100, 100000, 10, is_advanced=True)

for root, dirs, files in os.walk(path_some_data):
    for elem in os.scandir(root):
        name_elem = elem.name
        if name_elem not in dirs:
            for key in some_data_files_sizes_adv.keys():
                if elem.stat().st_size <= key:
                    some_data_files_sizes_adv[key][0] += 1
                    ext = name_elem[name_elem.rfind('.'):]
                    if ext not in some_data_files_sizes_adv[key][1]:
                        some_data_files_sizes_adv[key][1].append(ext)
                    break

print('{')
for key, value in some_data_files_sizes_adv.items():
    print(f'\t{key}: {value}', sep='\n')
print('}')
with open('task_07_5_summary.json', mode='w', encoding='utf-8') as file:
    json.dump(some_data_files_sizes_adv, file)
