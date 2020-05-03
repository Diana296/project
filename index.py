import os
import collections
import shutil
import string

path = ""

pictures = ['.png', '.jpeg', '.gif', '.svg', '.jpg']
programs = ['.py', '.js', '.html', '.css', '.java', '.cs', '.m', '.json']
documents = ['.pdf', '.docx', '.txt', 'doc']
films = ['.mp4', '.avi', '.mov', '.webm']
executables = ['.exe', '.bin']
music = ['.mp3', '.wav']


def read_files():
    # Вводим путь папки/директории
    # Возвращает список файлов в соответствующей папке/директории
    print("Введите полный путь папки:")
    global path
    local_path = input()
    path = local_path
    return os.listdir(local_path)


def define_type(file_format):
    if file_format in pictures:
        return 'pictures'
    if file_format in programs:
        return 'programs'
    if file_format in documents:
        return 'documents'
    if file_format in films:
        return 'films'
    if file_format in music:
        return "music"


def make_dirs(filelist):
    for i in filelist:
        print(i)
        if define_type(get_file_extension(i)) == "pictures":
            try:
                os.mkdir(path + "\pictures")
            except FileExistsError:
                print("Директория уже существует, но ничего страшного")
            shutil.move("".join([path, '\\', i]), path + "\pictures")
        elif define_type(get_file_extension(i)) == "programs":
            try:
                os.mkdir(path + "\programs")
            except FileExistsError:
                print("Директория уже существует, но ничего страшного")
            shutil.move("".join([path, '\\', i]), path + "\programs")
        elif define_type(get_file_extension(i)) == "documents":
            try:
                os.mkdir(path + "\documents")
            except FileExistsError:
                print("Директория уже существует, но ничего страшного")
            shutil.move("".join([path, '\\', i]), path + "\documents")
        elif define_type(get_file_extension(i)) == "films":
            try:
                os.mkdir(path + "\\films")
            except FileExistsError:
                print("Директория уже существует, но ничего страшного")
            shutil.move("".join([path, '\\', i]), path + "\\films")
        elif define_type(get_file_extension(i)) == "music":
            try:
                os.mkdir(path + "\music")
            except FileExistsError:
                print("Директория уже существует, но ничего страшного")
            shutil.move("".join([path, '\\', i]), path + "\music")





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
    print(filelist)
    filesCounter = 0
    for i in filelist:
        if '.' in i:
            filesCounter += 1
    # принимает список папок и файлов
    # возвращает словарик с количество файлов каждого расширения и количеством папок в директории
    counter = collections.Counter()
    for item in filelist:
        if item[0] == '.':
            continue
        counter[get_file_extension(item)] += 1
    return counter, filesCounter, len(filelist) - filesCounter


def make_report(data):
    global path
    print("Различных файлов в данной директории:", data[1])
    print("Различных папок в данной директории:", data[2])
    print("Файлов различных расширений в данной директории:", data[0])
    print("Хотите ли вы раскидать все файлы по соответсвующим директориям: Да/Нет")
    ans = input()
    if ans == "Да":
        make_dirs(os.listdir(path))


make_report(parse_file_list(read_files()))
