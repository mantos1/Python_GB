import sqlite3
import json as jn
import xml.etree.ElementTree as ET
import csv
import os
import xmltodict

file = "data.db"
try:
  conn = sqlite3.connect(file)
  cur = conn.cursor()
except:
  print("БД data.db не найдена!")
finally:
    def create_tb_data():
        cur.execute("drop table if exists Employee")
        cur.execute("drop table if exists Employee_Salary")
        # cur.execute("drop table IF EXISTS Employee_Dismissed")
        cur.execute("drop table if exists Employee_Info")

        conn.commit()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Employee(
           ID INTEGER PRIMARY KEY 
           ,Firstname TEXT
           ,Lastname TEXT
           ,Phone INTEGER
        ); 
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Employee_Salary(
            Employee_ID INTEGER
            ,Salary DOUBLE
        );  
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Employee_Info(
            Employee_ID INTEGER
            ,Position TEXT
            ,Active BIT
        );  
        """)
        conn.commit()

        # cur.execute("SELECT count(1) FROM Employee")
        # data = cur.fetchall()
        # for r in data:
        #     if r[0] == 0:
        employee = [('Евгений', 'Сычев', '9183423555')
            , ('Афанасий', 'Иванов', '9183422555')
            , ('Аркадий', 'Петров', '9183423111')
            , ('Георгий', 'Ионин', '9183424355')
            , ('Денис', 'Зхарченко', '9183423655')
            , ('Мария', 'Андреенко', '9183423555')
            , ('Наталья', 'Ананченко', '9183427755')
            , ('Максим', 'Малаев', '9183993555')
            , ('Антон', 'Куцов', '9183407355')]
        cur.executemany("INSERT INTO Employee (Firstname, Lastname, Phone) VALUES(?, ?, ?)", employee)

        salary = [('1', '25000')
            , ('2', '35000')
            , ('3', '50000')
            , ('4', '25000')
            , ('5', '20000')
            , ('6', '25000')
            , ('7', '35000')
            , ('8', '100000')
            , ('9', '50000')]
        cur.executemany("INSERT INTO Employee_Salary (Employee_ID, Salary) VALUES(?, ?)", salary)

        status = [('1', 'Специалист', 'True')
            , ('2', 'Младший специалист', 'True')
            , ('3', 'Руководитель группы', 'True')
            , ('4', 'Специалист', 'True')
            , ('5', 'Стажер', 'True')
            , ('6', 'Специалист', 'False')
            , ('7', 'Младший специалист', 'True')
            , ('8', 'Директор', 'True')
            , ('9', 'Руководитель группы', 'False')]
        cur.executemany("INSERT INTO Employee_Info (Employee_ID, Position, Active) VALUES(?, ?, ?)", status)
        conn.commit()
        conn.close()
        return "Таблицы с данным пересозданны!"
        # cur.execute("drop table phonebook")
        # conn.commit()

# def import_from_file(type = 0):
#     # 0 - импорт из new_data.json
#     # 1 - импорт из new_data.xml
#     c = 0
#     query = "INSERT INTO phonebook (name, phone) VALUES(?, ?)"
#
#     if type == 0:
#         with open("new_data.json", "r", encoding = "UTF8") as write_file:
#             data = jn.load(write_file)
#             columns = ['name', 'phone']
#
#             for row in data:
#                 cur.execute(f"SELECT count(1) FROM phonebook WHERE name = '{row['name']}' AND phone = '{row['phone']}'")
#                 data = cur.fetchall()
#                 for r in data:
#                     if r[0] == 0:
#                         keys = tuple([row[c].title() if c == 'name' else row[c][1:] if row[c][0] != '9' else row[c] for c in columns])
#                         cur.execute(query, keys)
#                         conn.commit()
#                 c += 1
#                 # conn.close()
#     elif type == 1:
#         tree = ET.parse('new_data.xml')
#         root = tree.getroot()
#         for i in root:
#             keys = (i[0].text.title(), i[1].text[1:] if i[1].text[0] != '9' else i[1].text )
#             cur.execute(query, keys)
#             conn.commit()
#             c += 1
#     conn.close()

    # with open('data.csv', 'r') as fin:  # `with` statement available in 2.5+
    #     # csv.DictReader uses first line in file for column headings by default
    #     dr = csv.DictReader(fin)  # comma is default delimiter
    #     to_db = [(i['col1'], i['col2']) for i in dr]
    #
    # cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
    # con.commit()
    # con.close()


    # def import_one_file_csv_to_sqlite():
    #
    #     con = sqlite3.connect('D:/2021_8_16_oborot/UL11.db')
    #     cur = con.cursor()
    #
    #     with open('D:/2021_8_16_oborot/part2/19_your_csv_file.csv', 'r', encoding='utf-8') as f_open_csv:
    #         rows = csv.reader(f_open_csv, delimiter="|")
    #
    #         for row in rows:
    #             cur.execute('INSERT INTO oborot_2019_fns12 VALUES (?, ?, ?, ?)', row)
    #
    #     con.commit()
    #     con.close()

        # >> > import json
    # >> > for country in countries:
    #     ...
    #     c.execute("insert into countries values (?, ?)",
    #               ...[country['id'], json.dumps(country)])
    # ...
    # conn.commit()
    # >> > conn.close()

    # return f"Успешно обработано {c} номера(ов)!"

def delete_export_file(mask_name = "export_data", ext = ['csv','xml','json']):
    ext_ = []
    ext_ = ext
    for e in ext_:
        file = mask_name + "." + e
        if os.path.isfile(file):
            os.remove(file)


def export_into_file(type = 0, name = "", lastname = "", phone = "", with_open = 0):
    sql = ""
    sql_name = f"""AND E.FirstName LIKE '%{name}%'""" if name != "" else ""
    sqllastname = f"""AND E.Lastname LIKE '%{lastname}%'""" if lastname != "" else ""
    sqlphone = f"""AND E.Phone LIKE '%{phone}%'""" if phone != "" else ""
    sql = """
          SELECT 
              E.ID
              ,E.FirstName AS Имя
              ,E.Lastname AS Фамилия
              ,EI.Position AS Должность
              ,E.Phone AS Телефон
              ,CASE 
                  WHEN EI.Active <> "False" THEN "Работает"
                  WHEN EI.Active = "False" THEN "Уволен"
              END AS Активность
              ,ES.Salary AS [Целевой Уровень (руб)]
          FROM Employee               AS E     
          INNER JOIN Employee_Info    AS EI   ON EI.Employee_ID = E.ID
          INNER JOIN Employee_Salary  AS ES   ON ES.Employee_ID = E.ID
          WHERE 1=1
      """ + sql_name + sqllastname + sqlphone
    dt = cur.execute(sql)
    data = cur.fetchall()
    export_file = "export_data"

    if type == 0:
        with open(f"{export_file}.json", "w", encoding = "UTF8") as write_file:
            jsonfile = []
            columns = [i[0] for i in dt.description]
            for r in data:
                dct = {}
                for key, value in enumerate(r):
                    dct[columns[key]] = value
                jsonfile.append(dct)
            jn.dump(jsonfile, write_file, indent=4, ensure_ascii=False)
        export_file = export_file + ".json"
    if type == 1:
        dict = {}
        columns = [i[0] for i in dt.description[1:]]
        for key, r in enumerate(data):
            dct = {}
            for key, value in enumerate(r[1:]):
                dct[columns[key]] = value
            dict[f"Сотрудник {r[0]}"] = dct

        root = ET.Element('root')
        for item in dict:
            employee = ET.SubElement(root, item )
            for i in dict[item]:
                ET.SubElement(employee, i).text = str(dict[item][i])
        tree = ET.ElementTree(root)

        tree.write(f"{export_file}.xml", xml_declaration=True , encoding='utf-8')
        export_file = export_file + ".xml"
    # xmldata = {
    #     'Student': {
    #         '@name': 'Ravi',
    #         '@age': 21,
    #         "college": "Anna University"
    #     }
    # }
    #
    # print(xmltodict.unparse(xmldata, pretty=True))
    if type == 2:
        with open(f"{export_file}.csv", "w", newline="") as csvfile:
            wtr = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_ALL)
            wtr.writerow([i[0] for i in dt.description])
            for row in data:
                wtr.writerow(row)
        export_file = export_file + ".csv"
    conn.close()

    # import sqlite3
    # from xlsxwriter.workbook import Workbook
    # workbook = Workbook('output.xlsx')
    # worksheet = workbook.add_worksheet()
    # # Pass in the database path, db.s3db or test.sqlite
    # conn = sqlite3.connect('db.s3db_or_test.sqlite')
    # c = conn.cursor()
    # mysel = c.execute("select * from question")
    # for i, row in enumerate(mysel):
    #     for j, value in enumerate(row):
    #         worksheet.write(i, j, value)
    # workbook.close()
    return f"Данные экспортированы в {export_file}!"
    # os.startfile(export_filea) #if with_open == 1 else ""
    # os.system(r'"C:/Users/HOME_PC/PycharmProjects/Python_Lessons/Lesson_8/export_data.json"')

#delete_export_file()
# export_into_file(1)