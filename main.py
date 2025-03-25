import pickle
from os import path

BASE_FILE = 'data.pkl'


def welcome():
    print('~ Вас приветствует Список Дел ~')

def create_base():
    base_template = {
        'List_Tasks': ['task 1', 'task 2', 'task 3']
    }

    if not path.exists(BASE_FILE):
        with open(BASE_FILE, 'wb') as file:
            pickle.dump(base_template, file)


def get_base() -> dict:
    with open(BASE_FILE, 'rb') as file:
        return pickle.load(file)


def show_menu():
    print('1. Добавить задачу')
    print('2. Полный список дел')
    print('3. Удалить задачу')
    print('q. Выход')


if __name__ == '__main__':
    create_base()
    welcome()
    show_menu()
    print(get_base())
    print(__name__)