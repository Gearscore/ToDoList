import pickle
from os import path

BASE_FILE = 'data.pkl'


def show_menu():
    "Показать приветствие и меню"
    print('~ You are welcomed by a list of affairs ~\n')
    print('1. Add the task')
    print('2. A complete list of affairs')
    print('3. Delete the task')
    print('q. Exit')


def create_base():
    "Создать файл базы данных"
    template = {
        'List_Tasks': []
    }

    if not path.exists(BASE_FILE):
        with open(BASE_FILE, 'wb') as file:
            pickle.dump(template, file)


def get_base() -> dict:
    "Получить данные из файла базы данных"
    with open(BASE_FILE, 'rb') as file:
        return pickle.load(file)


def save_base(task: str, data: dict):
    data['List_Tasks'].append(task)
    with open(BASE_FILE, 'wb') as file:
        pickle.dump(data, file)


def user_input() -> str:
    "Ввод пользователя"
    while True:
        s = input("\nYour Select: ")
        if not (len(s) == 1 and s in ('1', '2', '3', 'q', 'Q')):
            print(f"invalid input not {('1', '2', '3', 'q')}")
        else:
            return s


# Конструкция if __name__ == '__main__': — это важный идиом в Python, который
# определяет, выполняется ли файл напрямую или импортируется как модуль.
if __name__ == '__main__':
    create_base()
    data_base = get_base()

    while True:
        show_menu()
        result_input = user_input()
