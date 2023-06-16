import pyodbc

from config import Config
from my_database import MyDatabase


class DatabaseReader:

    def __init__(self) -> None:
        self.db = MyDatabase()
        self.cursor = self.db.get_connection()

    def is_empty(self, table_name):
        try:
            sql_select = f"""SELECT COUNT(*) FROM [{Config.DB_NEW_NAME}].[dbo].[{table_name}]"""
            self.cursor.execute(sql_select)
            result = self.cursor.fetchone()[0]
            if result == 0:
                empty_table = True
            else:
                empty_table = False
        except pyodbc.Error as e:
            print(f"There is a problem with read data: {e}")
        else:
            return empty_table

    def sql_get_all(self, sql_execute):
        try:
            self.cursor.execute(sql_execute)
            result = self.cursor.fetchall()
        except pyodbc.Error as e:
            print(f"There is a problem with read data: {e}")
        else:
            self.db.close_connection()
            return result