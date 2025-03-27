import pickle
from os import path
from sys import exit

BASE_FILE = 'data.pkl'


def show_menu():
    "Показать приветствие и меню"
    print('~ You are welcomed by a list of tasks ~\n')
    print('1. Add the task')
    print('2. A complete list of tasks')
    print('3. Delete the task')
    print('4. Clean the list of tasks')
    print('q. Exit')


def cleaning_screen():
    "ANSI-коды для очистки экрана"
    print("\033[H\033[J", end="")


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


def save_base(data: dict):
    "Сахранить в файл базы данных"
    with open(BASE_FILE, 'wb') as file:
        pickle.dump(data, file)


def user_input() -> str:
    "Ввод пользователя и проверка корректности"
    while True:
        s = input("\nYour Select: ")
        if not (len(s) == 1 and s in ('1', '2', '3', '4', 'q', 'Q')):
            print(f"invalid input not {('1', '2', '3', '4', 'q')}")
        else:
            return s


def add_task():
    "сохранение задачи в базе"
    task = input('Enter The Task: ')
    data_base = get_base()
    data_base['List_Tasks'].append(task)
    save_base(data_base)
    print("The task is added to the list\n")


def show_list_tasks():
    "показать список задач"
    data_base = get_base()
    list_tasks = data_base['List_Tasks']
    if not list_tasks:
        print("Empty list\n")
    else:
        print()
        for i in range(len(list_tasks)):
            print(f"{i + 1}. {list_tasks[i]}")
        print()


def clean_list_tasks():
    "Очищает список задач"
    data_base = get_base()
    data_base['List_Tasks'] = []
    save_base(data_base)
    print("Empty\n")


def delete_task():
    "Удаление задачи"
    data_base = get_base()
    list_tasks = data_base['List_Tasks']
    while True:
        index_task = int(input("Indicate the number of the deleted task: "))
        if not list_tasks:
            print("Empty\n")
            break
        if 1 <= index_task <= len(list_tasks):
            res = list_tasks.pop(index_task - 1)
            print(f"Delete task - {res}\n")
            break
        else:
            print("There is no such task\n")
    save_base(data_base)


# Конструкция if __name__ == '__main__': — это важный идиом в Python, который
# определяет, выполняется ли файл напрямую или импортируется как модуль.
if __name__ == '__main__':
    create_base()

    while True:
        # cleaning_screen()
        show_menu()
        result_input = user_input()
        match result_input:
            case "1":
                add_task()
            case "2":
                show_list_tasks()
            case "3":
                delete_task()
            case "4":
                clean_list_tasks()
            case "q" | "Q":
                exit()
