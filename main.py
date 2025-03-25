import pickle
from os import path

NAME_BASE = 'data.pkl'
print('~ Вас приветствует Список Дел ~')


def create_base():
    data_base = {
        'List_Tasks': ['task 1', 'task 2', 'task 3']
    }

    if not path.exists(NAME_BASE):
        with open(NAME_BASE, 'wb') as file:
            pickle.dump(data_base, file)


create_base()


def get_base() -> dict:
    with open(NAME_BASE, 'rb') as file:
        return pickle.load(file)


print(get_base())


def show_menu():
    print('1. Добавить задачу')
    print('2. Полный список дел')
    print('3. Удалить задачу')
    print('q. Выход')


show_menu()
