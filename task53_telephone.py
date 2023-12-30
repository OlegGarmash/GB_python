# Открыть файл
# сохранить файл
# Создание контакта
# Изм контакт
# Найти контакт
# Удалить контакт
# показать контакт
# выход
def menu_main():
    print('\nВыберете пункт меню:')
    print('Открыть файл - 1')
    print('Сохранить файл - 2')
    print('Создать контакт - 3')
    print('Изменить контакт - 4')
    print('Поиск контакта - 5')
    print('Удалить контакт - 6')
    print('Показать все контакты - 7')
    print('Скопировать контакт - 8')
    print('Выход - 0')


def menu_edit_contact():
    print('\nВыберете пункт меню:')
    print('Изменить ФИО - 1')
    print('Изменить телефон - 2')
    print('Изменить комментарий - 3')
    print('Выход - 0')


def open_file(file_name):
    with open(file_name) as file:
        data = {}
        for line in file:
            key, *value = line.split()
            key = int(key)
            data[key] = value
    return data


def save_file(data, file_name):
    with open(file_name, 'w') as file:
        for key, value in data.items():
            file.write(f'{key} {value[0]} {value[1]} {value[2]}\n')


def create_contact(contact_list):
    data = [input('\nВведите ФИО: '), input('Введите номер телефона: '), input('Введите комментарий: ')]
    if len(contact_list) > 0:
        contact_list[list(contact_list.keys())[len(contact_list) - 1] + 1] = data
    else:
        contact_list[1] = data
    return contact_list


def edit_contact(contact_list):
    id_contact = int(input('\nВведите id контакта для редактирования: '))
    if id_contact not in contact_list:
        print(f'Контакт с id {id_contact} не найден!')
    else:
        menu_edit_contact()
        a = int(input('-> '))
        while a != 0:
            contact_list[id_contact][a - 1] = input('Введите новое значение: ')
            print(*contact_list[id_contact], sep=', ')
            menu_edit_contact()
            a = int(input('-> '))
    return contact_list


def find_contact(contact_list):
    find_data = input('Введите данные для поиск:\n')
    count = 0
    for key, value in contact_list.items():
        if find_data.lower() in str(value).lower():
            print(f'id {key}:', end='\t')
            print(*list(value), sep=', ')
            count += 1
    if count == 0:
        print('Контакт не найден!')


def delete_contact(contact_list):
    id_contact = int(input('\nВведите id контакта для удаления: '))
    if id_contact not in contact_list:
        print(f'Контакт с id {id_contact} не найден!')
    else:
        del contact_list[id_contact]
    return contact_list


def show_contact(contact_list):
    for key, value in contact_list.items():
        print(f'id {key}:', end='\t')
        print(*list(value), sep=', ')


def copy_contact(contact_list):
    id_contact = int(input('\nВведите id контакта для копирования: '))
    if id_contact not in contact_list:
        print(f'Контакт с id {id_contact} не найден!')
    else:
        #file_name = input('\nВведите имя файла для сохранения контакта: ')
        file_name = 'task53.txt'
        with open(file_name) as file:
            data = {}
            for line in file:
                key, *value = line.split()
                key = int(key)
                data[key] = value
            count = 0
            for k, v in data.items():
                if contact_list[id_contact] == v:
                    count += 1
        if count != 0:
            print(f'Контакт уже существует в файле {file_name}')
        else:
            with open(file_name, 'a') as file:
                file.write(
                    f'{id_contact} {contact_list[id_contact][0]} {contact_list[id_contact][1]} {contact_list[id_contact][2]}\n')


menu_main()
a = int(input('-> '))
while a != 0:
    if a == 1:
        main_data = open_file('task53_main.txt')
    elif a == 2:
        save_file(main_data, 'task53_main.txt')
    elif a == 3:
        create_contact(main_data)
    elif a == 4:
        edit_contact(main_data)
    elif a == 5:
        find_contact(main_data)
    elif a == 6:
        delete_contact(main_data)
    elif a == 7:
        show_contact(main_data)
    elif a == 8:
        copy_contact(main_data)
    menu_main()
    a = int(input('-> '))
print(main_data)
