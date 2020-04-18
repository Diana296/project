import os
import collections


def read_files():
    # Вводим путь папки/директории
    # Возвращает список файлов в соответствующей папке/директории
    print("Введите полный путь папки:")
    return os.listdir(input())


def get_file_extension(filename):
    # функция возвращает расширение файла
    # если найдена папка, то функция вернёт 'other folders'
    pos = None
    for i in range(0, len(filename)):
        if filename[i] == '.':
            pos = i
    if pos is None:
        return "other folders"
    return filename[pos:: 1]


def parse_file_list(filelist):
    # принимает список папок и файлов
    # возвращает словарик с количество файлов каждого расширения и количеством папок в директории
    counter = collections.Counter()
    for item in filelist:
        if item[0] == '.':
            continue
        counter[get_file_extension(item)] += 1
    return counter


print(parse_file_list(read_files()))
print(len(os.listdir(input())))
