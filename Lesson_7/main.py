import controller

# Пересоздание таблицы справчоника в data.db
def button_create_data_db():
    controller.create_data()

def button_phonebook():
    controller.get_phonebook()

def button_import():
    controller.get_import()

def button_export():
    controller.get_export()

