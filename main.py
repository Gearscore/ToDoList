import pickle
from os import path
from sys import exit

BASE_FILE = 'data.pkl'


def welcome():
    "Приветствие"
    print('~ You are welcomed by a list of tasks ~\n')


def show_menu(show_flag: bool = True) -> dict:
    "Показать меню"
    menu = {
        "1": "Add the task",
        "2": "A complete list of tasks",
        "3": "Delete the task",
        "4": "Clean the list of tasks",
        "q": "Exit"
    }
    if show_flag:
        for k, v in menu.items():
            print(f"{k}. {v}")
    return menu


def stop_waiting_user():
    "Остановка программы ожидание действий пользователя"
    input("continue Enter...")


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
    "Сахранить данные в файл базы данных"
    with open(BASE_FILE, 'wb') as file:
        pickle.dump(data, file)


def user_input() -> str:
    "Ввод пользователя и проверка корректности"
    while True:
        s = input("\nYour Select: ").lower()
        if not (len(s) == 1 and s in show_menu(show_flag=False).keys()):
            print(f"invalid input not ({', '.join(show_menu(show_flag=False).keys())})")
        else:
            return s


def add_task():
    "сохранение задачи в базе"
    while True:
        task = input('Enter The Task (0-cancel): ')
        if task == '0':
            print("The operation is canceled\n")
            return
        if len(task) != task.count(" ") and task != "":
            break
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
    show_list_tasks()
    data_base = get_base()
    list_tasks = data_base['List_Tasks']
    while True:
        index_task = input("Indicate the number of the deleted task (0-cancel): ")
        if index_task == "0":
            print("The operation is canceled\n")
            return
        if not list_tasks:
            print("Empty\n")
            break
        if index_task.isdigit():
            index_task = int(index_task)
        else:
            print("Error not is numbers")
            continue
        if 1 <= index_task <= len(list_tasks):
            res = list_tasks.pop(index_task - 1)
            print(f"Delete task - {res}\n")
            save_base(data_base)
        else:
            print("There is no such task\n")



# Конструкция if __name__ == '__main__': — это важный идиом в Python, который
# определяет, выполняется ли файл напрямую или импортируется как модуль.
if __name__ == '__main__':
    create_base()

    while True:
        welcome()
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
            case "q":
                exit()
        stop_waiting_user()
        cleaning_screen()
