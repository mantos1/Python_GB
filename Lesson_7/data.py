import sqlite3
import json as jn
import xml.etree.ElementTree as ET

conn = sqlite3.connect('data.db')
cur = conn.cursor()

def create_tb_data():
    cur.execute("drop table phonebook")
    conn.commit()
    cur.execute("""CREATE TABLE IF NOT EXISTS phonebook(
       id INTEGER PRIMARY KEY,
       name TEXT,
       phone INTEGER);
    """)
    conn.commit()

    # cur.execute("DELETE FROM phonebook")
    # conn.commit()

    cur.execute("SELECT count(1) FROM phonebook")
    data = cur.fetchall()
    for r in data:
        if r[0] == 0:
            phonebook = [('Евгений', '9183423555')
                         ,('Афанасий', '9183422555')
                         ,('Аркадий', '9183423111')
                         ,('Георгий', '9183424355')
                         ,('Денис', '9183423655')
                         ,('Мария', '9183423555')
                         ,('Наталья', '9183427755')
                         ,('Максим', '9183993555')
                         ,('Антон', '9183407355')]
            cur.executemany("INSERT INTO phonebook (name, phone) VALUES(?, ?)", phonebook)
            conn.commit()
    return "Таблица с данным пересозданна!"
    # cur.execute("drop table phonebook")
    # conn.commit()


def import_from_file(type = 0):
    # 0 - импорт из new_data.json
    # 1 - импорт из new_data.xml
    c = 0
    query = "INSERT INTO phonebook (name, phone) VALUES(?, ?)"

    if type == 0:
        with open("new_data.json", "r", encoding = "UTF8") as write_file:
            data = jn.load(write_file)
            columns = ['name', 'phone']

            for row in data:
                cur.execute(f"SELECT count(1) FROM phonebook WHERE name = '{row['name']}' AND phone = '{row['phone']}'")
                data = cur.fetchall()
                for r in data:
                    if r[0] == 0:
                        keys = tuple([row[c].title() if c == 'name' else row[c][1:] if row[c][0] != '9' else row[c] for c in columns])
                        cur.execute(query, keys)
                        conn.commit()
                c += 1
                # conn.close()
    elif type == 1:
        tree = ET.parse('new_data.xml')
        root = tree.getroot()
        for i in root:
            keys = (i[0].text.title(), i[1].text[1:] if i[1].text[0] != '9' else i[1].text )
            cur.execute(query, keys)
            conn.commit()
            c += 1
    return f"Успешно обработано {c} номера(ов)!"

def export_into_file(type = 0):
    cur.execute("SELECT * FROM phonebook ORDER BY name")
    data = cur.fetchall()
    if type == 0:
        with open("export_data.json", "w", encoding = "UTF8") as write_file:
            jsonfile = []
            for r in data:
                jsonfile.append({"name": r[1], "phone": r[2]})
            jn.dump(jsonfile, write_file, indent=4, ensure_ascii=False)
    if type == 1:
        root = ET.Element("root")
        for key, value in enumerate(data):
            item = ET.SubElement(root, "item", name = f"item{key+1}")
            ET.SubElement(item, "name").text = value[1]
            ET.SubElement(item, "phone").text = str(value[2])
        tree = ET.ElementTree(root)
        tree.write("export_data.xml", xml_declaration=True , encoding='utf-8')
    return "Справочник экспортирован!"


