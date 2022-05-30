import os
import shutil

path_my_project = os.path.abspath(os.path.join('..', 'task_07_2', 'my_project'))
path_to_templates_folder = os.path.join(path_my_project, 'templates')
if os.path.exists(path_my_project):
    for root, directories, files in os.walk(path_my_project):
        for directory in directories:
            if directory == 'templates':
                path_to_template = os.path.join(root, directory)
                shutil.copytree(path_to_template, path_to_templates_folder, dirs_exist_ok=True)
    print(f'Шаблоны собраны в: {path_my_project}')
else:
    print(f'Директории {path_my_project} не существует.')
