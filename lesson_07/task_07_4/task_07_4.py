import os
from functions import dict_creation

path_some_data = os.path.abspath('some_data')
some_data_files_sizes = dict_creation(100, 100000, 10)

for root, dirs, files in os.walk(path_some_data):
    for elem in os.scandir(root):
        if elem.name not in dirs:
            for key in some_data_files_sizes.keys():
                if elem.stat().st_size <= key:
                    some_data_files_sizes[key] += 1
                    break

print('{')
for key, value in some_data_files_sizes.items():
    print(f'\t{key}: {value}', sep='\n')
print('}')
