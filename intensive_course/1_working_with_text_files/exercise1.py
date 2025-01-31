#Exercise1
# #task1
# def input_and_print_to_do():
#     data = input('Введите дату в формате чч.мм.гггг: ')
#     task_description = input('Введите описание задачи: ')
#     print(f'{data} {task_description}')

def input_to_do_item(IsList: bool) -> str | tuple:
    data = input('Введите дату в формате чч.мм.гггг: ')
    task_description = input('Введите описание задачи: ')
    if IsList:
        return f'{data} {task_description}'
    else:
        return (data, task_description) #for task3

def print_to_do_list(to_do_list: list):
    for i in range(len(to_do_list)):
        print(to_do_list[i])

#task2
def input_to_do_list():
    to_do_list = list()
    for i in range(3):
        to_do_list.append(input_to_do_item())
    print_to_do_list(to_do_list)
#input_to_do_list()

#task3
def input_to_do_dict():
    to_do_dict = {}
    for i in range(3):
        data, task_description = input_to_do_item(False)
        to_do_dict[data] = task_description
    return to_do_dict

#print(input_to_do_dict())

#task4
def action_by_command():
    to_do_list = list()
    type_action = input("Введите одну команду из списка: 'help', 'add', 'print': ")

    while type_action == 'add':
        to_do_list.append(input_to_do_item(True))
        type_action = input("Введите одну команду из списка: 'help', 'add', 'print': ")

    if type_action == 'print':
        print_to_do_list(to_do_list)
    elif type_action == 'help':
        print("Это справка по программе")


action_by_command()




