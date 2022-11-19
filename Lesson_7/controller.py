import data
import view

def create_data():
    print(data.create_tb_data())

def get_phonebook():
    view.get_view_phonebook()

def get_import():
    a = input("Укажите в каком формате нужно импортировать данные: xml или json?\n")
    print(data.import_from_file(1 if a == 'xml' else 0))

def get_export():
    a = input("Укажите в каком формате нужно экспортировать данные: xml или json?\n")
    print(data.export_into_file(1 if a == 'xml' else 0))