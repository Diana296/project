import os
import collections
import shutil
import time
import tkinter as tk
from tkinter import scrolledtext


path = ""

pictures = ['.png', '.jpeg', '.gif', '.svg', '.jpg']
programs = ['.py', '.js', '.html', '.css', '.java', '.cs', '.m', '.json']
documents = ['.pdf', '.docx', '.txt', 'doc']
films = ['.mp4', '.avi', '.mov', '.webm']
executables = ['.exe', '.bin']
music = ['.mp3', '.wav']



def read_files(local_path):
    """
    Вводим путь папки/директории
    Возвращает список файлов в соответствующей папке/директории
    """
    global path
    files = []
    path = local_path
    tree = os.walk(path)
    for i in tree:
        for j in i[2]:
            files.append(i[0] + "/" + j)
    return files


def define_type(file_format):
    """
    Функция принимает на вход расширение файла
    Возвращает название папки для данного расширения
    """
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


def create_dir(file_name, dirname, date):
    """
    Функция принимает название файла, дату его создания и директорию, в которую
    этот файл необходимо закинуть
    Возвращает: -
    """
    try:
        os.mkdir(path + "/" + dirname)
    except FileExistsError:
        print()
    try:
        os.mkdir(path + "/" + dirname + "/" + date[0])
    except FileExistsError:
        print()
    try:
        os.mkdir(path + "/" + dirname + "/" + date[0] + "/" + date[1])
    except FileExistsError:
        print()
    #  Перемещаем файл в соответствующую директорию
    shutil.move(file_name, path + "/" + dirname + "/" + date[0] + "/" + date[1])


def make_dirs(file_list):
    """
    Функция принимаем список файлов
    Определяет тип файла, создаёт директорию и
    перекидывает файл в соответствующую директорию
    """
    for i in file_list:
        if define_type(get_file_extension(i)) == "pictures":
            create_dir(i, "pictures", parse_date(i))
        elif define_type(get_file_extension(i)) == "programs":
            create_dir(i, "programs", parse_date(i))
        elif define_type(get_file_extension(i)) == "documents":
            create_dir(i, "documents", parse_date(i))
        elif define_type(get_file_extension(i)) == "films":
            create_dir(i, "films", parse_date(i))
        elif define_type(get_file_extension(i)) == "music":
            create_dir(i, "music", parse_date(i))
        else:
            create_dir(i, "other", parse_date(i))


def get_file_extension(filename):
    """
    Принимает имя файла
    Возвращает расширение файла
    Если найдена папка, то функция вернёт 'other folders'
    """
    pos = None
    for i in range(0, len(filename)):
        if filename[i] == '.':
            pos = i
    if pos is None:
        return "other folders"
    return filename[pos:: 1]


def parse_file_list(file_list):
    """
    Функция принимает на вход: список путей до файлов
    Возвращает: количество расширений, количество файлов, количество папок  и сам список файлов
    """
    files_counter = 0
    for i in file_list:
        if '.' in i:
            files_counter += 1
    counter = collections.Counter()
    for item in file_list:
        if item[0] == '.':
            continue
        counter[get_file_extension(item)] += 1
    make_dirs(file_list)
    return counter, files_counter, len(file_list) - files_counter, file_list


# def make_report(data):
#     """
#     Функция принимает результат функции  parse_file_list()
#     Создаёт текстовый отчёт о файлах
#     """
#     global path
#     print("Различных файлов в данной директории:", data[1])
#     print("Различных папок в данной директории:", data[2])
#     print("Файлов различных расширений в данной директории:", data[0])
#     make_dirs(data[3])


def parse_date(file_path):
    """
    Принимает путь к файлу
    Возращает год и месяц создания файла
    """
    #  работает корректно только под windows
    date = time.ctime(os.path.getctime(file_path))
    year = date[-4:]
    month = date[4:7]
    return year, month


def start():
    file_path = input_entry.get()
    #  make_report(parse_file_list(read_files(file_path)))
    data = parse_file_list(read_files(file_path))
    listBox = tk.Listbox()
    listBox = scrolledtext.ScrolledText(width=85,height=10)
    listBox.insert(tk.END, "Различных файлов в данной директории:" + str(data[1]))
    listBox.insert(tk.END, "Различных папок в данной директории:" + str(data[2]))
    listBox.insert(tk.END, "Файлов различных расширений в данной директории" + str(data[0]))
    listBox.grid(row=3, columnspan=5)
    

if __name__ == '__main__':
    root = tk.Tk() 
    root.geometry('800x400')
    root.title("Работа с файлами")
    textbox = tk.Label(text="Введите полный путь до директории", font=("Century", 14)) 
    textbox.grid(column=0, row=0)
    input_entry = tk.Entry(width=70)
    input_entry.grid(column=1, row=0)
    button = tk.Button(text='Отсортировать содержимое папки', bg="pink", fg="white", command=start)
    button.grid(column=0, row=1, columnspan=2, padx=10, pady=10)
    root.mainloop()
