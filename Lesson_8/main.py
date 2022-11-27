import controller

# Пересоздание таблицы справчоника в data.db
def button_remove_export_files():
    controller.remove_export_files()
def button_create_data_db():
    controller.create_data()

def button_employee_ifo():
    controller.get_employee_info()

def button_export():
    controller.get_export()

button_employee_ifo()