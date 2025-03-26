import pickle
from os import path

BASE_FILE = 'data.pkl'


def welcome():
    "Приветствие"
    print('~ You are welcomed by a list of affairs ~\n')


def show_menu():
    "Показать меню"
    print('1. Add the task')
    print('2. A complete list of affairs')
    print('3. Delete the task')
    print('q. Exit')


def create_base():
    "Создать файл базы данных"
    template = {
        'List_Tasks': ['task 1', 'task 2', 'task 3']
    }

    if not path.exists(BASE_FILE):
        with open(BASE_FILE, 'wb') as file:
            pickle.dump(template, file)


def get_base() -> dict:
    "Получить данные из файла базы данных"
    with open(BASE_FILE, 'rb') as file:
        return pickle.load(file)


# Конструкция if __name__ == '__main__': — это важный идиом в Python, который
# определяет, выполняется ли файл напрямую или импортируется как модуль.
if __name__ == '__main__':
    create_base()
    data_base = get_base()
    welcome()

    while True:
        show_menu()
        user_input = input("\nYour Select: ")
