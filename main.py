import pickle
from os import path

BASE_FILE = 'data.pkl'


def welcome():
    print('~ You are welcomed by a list of affairs ~')


def show_menu():
    print('1. Add the task')
    print('2. A complete list of affairs')
    print('3. Delete the task')
    print('q. Exit')


def create_base():
    template = {
        'List_Tasks': ['task 1', 'task 2', 'task 3']
    }

    if not path.exists(BASE_FILE):
        with open(BASE_FILE, 'wb') as file:
            pickle.dump(template, file)


def get_base() -> dict:
    with open(BASE_FILE, 'rb') as file:
        return pickle.load(file)


if __name__ == '__main__':
    create_base()
    welcome()
    show_menu()
    data_base = get_base()
    print(data_base)
