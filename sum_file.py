import os


def create_new_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, 'xt'):
            print(f'Файл {file_name} успешно создан.')


def sort_files(file_names):
    dict_files = {}
    for file in file_names:
        with open(file, 'rt', encoding='UTF-8') as open_file:
            dict_files[file] = len(open_file.read())

    dict_files = dict(sorted(dict_files.items(), key=lambda item: item[1]))

    return dict_files


def insert_data(sum_name):
    sorted_files = sort_files([first_name_file, second_name_file, third_name_file])

    with open(sum_name, 'wt', encoding='UTF-8') as new_file:
        for file, lines in sorted_files.items():
            with open(file, 'rt', encoding='UTF-8') as open_file:
                new_file.writelines(f'{file}\n')
                new_file.writelines(f'{str(lines)}\n')
                new_file.writelines(f'{open_file.read()}\n')


sum_name_file = 'sum_file.txt'
first_name_file = '1.txt'
second_name_file = '2.txt'
third_name_file = '3.txt'

create_new_file(sum_name_file)
insert_data(sum_name_file)