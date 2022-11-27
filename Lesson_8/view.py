import sqlite3
import pandas as pd
# from IPython.display import display
from tabulate import tabulate as tb

file = "data.db"
try:
  conn = sqlite3.connect(file)
  cur = conn.cursor()
except:
  print("БД data.db не найдена!")
finally:
    def get_information(type = 0, name = "", lastname = "", phone = ""):
        # 0 - полная информация, 1 - список увлоеных и работающих, 2 - телефонный справочник
        sql = ""
        sql_name = f"""AND E.FirstName LIKE '%{name}%'""" if name != "" else ""
        sqllastname = f"""AND E.Lastname LIKE '%{lastname}%'""" if lastname != "" else ""
        sqlphone = f"""AND E.Phone LIKE '%{phone}%'""" if phone != "" else ""

        if type == 0:

            sql = """
                SELECT 
                    E.FirstName AS Имя
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
            """ + sql_name + sqllastname

            # dt = cur.execute(sql)
            # cols = [column[0] for column in dt.description]
            # results = pd.DataFrame.from_records(data=dt.fetchall(), columns=cols)
            # display(results)

            # df = pd.read_sql_query(sql, conn)
            # # df.style.background_gradient()
            # print(tb(df, headers='keys', tablefmt='rounded_grid'))

            # cur.execute(sql)
            # data = cur.fetchall()
            # for row in data:
            #     print(row)
        elif type == 1:

            sql = """
                SELECT 
                    E.FirstName AS Имя
                    ,E.Lastname AS Фамилия
                    ,EI.Position AS Должность 
                    ,CASE 
                        WHEN EI.Active <> "False" THEN "Работает"
                        WHEN EI.Active = "False" THEN "Уволен"
                    END AS Активность 
                FROM Employee               AS E     
                INNER JOIN Employee_Info    AS EI   ON EI.Employee_ID = E.ID
                INNER JOIN Employee_Salary  AS ES   ON ES.Employee_ID = E.ID
                WHERE 1=1
            """ + sql_name + sqllastname
        elif type == 2:

            sql = """
                  SELECT 
                      E.FirstName AS Имя
                      ,E.Lastname AS Фамилия
                      ,E.Phone AS Телефон
                  FROM Employee AS E
                  WHERE 1=1
              """ + sql_name + sqllastname + sqlphone

        df = pd.read_sql_query(sql, conn)
        print(tb(df, headers='keys', tablefmt='rounded_grid'))
        conn.close()




