import data
import view

def create_data():
    print(data.create_tb_data())

def get_employee_info():
    # 0 - полная информация, 1 - список увлоеных и работающих, 2 - телефонный справочник
    question = ""
    question = input(
        "Укажите тип запрашиваемой информации:\n\
    0 - Полная информация по сотрудникам\n\
    1 - Cписок увлоеных и работающих\n\
    2 - Телефонный справочник\n\
Для выхода введите 'q'\n").lower()
    if question == "q":
        return("Операция отменена!")
    name = ""
    lastname = ""
    phone = ""
    if input("Нужен ли поиск по фильтрам: yes/no?\n").lower() == "yes":
        name = input("Введите имя или нажмите Enter:\n")
        lastname = input("Введите фамилию или нажмите Enter:\n")
        phone = input("Введите телефон или его часть, либо нажмите Enter:\n")
    view.get_information(type=int(question), name=name, lastname=lastname, phone=phone)

def remove_export_files():
    data.delete_export_file()

def get_export():
    question = ""
    question = input(
        "Укажите в каком формате нужно экспортировать данные: xml, json или csv?\nДля выхода введите 'q'\n").lower()
    if question == "q":
        return("Операция отменена!")
    elif question == "xml":
        type = 1
    elif question == "json":
        type = 0
    else:
        type = 2
    name = ""
    lastname = ""
    phone = ""
    if input("Нужен ли поиск по фильтрам: yes/no?\n").lower() == "yes":
        name = input("Введите имя или нажмите Enter:\n")
        lastname = input("Введите фамилию или нажмите Enter:\n")
        phone = input("Введите телефон или его часть, либо нажмите Enter:\n")
    print(data.export_into_file(type=type, name=name, lastname=lastname, phone=phone))
