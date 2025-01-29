# Читаем введенную строку текста
input_string = input('Введите новую строку текста: ')

# Записываем введенную строку в конец файла
path_to_file = '/home/andrallex/python-ed/intensive_course/1_working_with_text_files/text_for_task_4.txt'
with open(path_to_file, 'a', encoding = 'utf-8') as file:
    file.write(f'\n {input_string}')
    
# Проверяем
with open(path_to_file, 'r', encoding = 'utf-8') as file:
    lines = [line for line in file.readlines()]
    print(f'Первая строка исходного текста: {lines[0]}')
    print(f'Последняя добавленная пользователем строка: {lines[-1]}')