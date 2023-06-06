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
