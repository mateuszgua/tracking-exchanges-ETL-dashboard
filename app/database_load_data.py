import pyodbc

from config import Config
from my_database import MyDatabase


class FillTables:

    def __init__(self) -> None:
        self.db = MyDatabase()
        self.cursor = self.db.get_connection()

    def fill_table(self, table_name, df):
        match table_name:
            case "indexData":
                sql = f"""INSERT INTO [{Config.DB_NEW_NAME}].[dbo].[indexData] VALUES (?,?,?,?,?,?,?,?,?)"""
            case "indexInfo":
                sql = f"""INSERT INTO [{Config.DB_NEW_NAME}].[dbo].[indexInfo] VALUES (?,?,?,?,?)"""
            case "indexProcessed":
                sql = f"""INSERT INTO [{Config.DB_NEW_NAME}].[dbo].[indexProcessed] VALUES (?,?,?,?,?,?,?,?,?,?)"""
        try:
            print(f"Load data in table: {table_name}")
            df = df.fillna('0')
            df_to_list = df.to_records().tolist()
            # self.cursor.fast_executemany = True
            self.cursor.executemany(sql, df_to_list)
            self.cursor.commit()
            self.cursor.close()
        except pyodbc.Error as e:
            print(
                f"There is a problem with load data in table {table_name} error: {e}")
        else:
            print(f"{len(df)} rows loaded successfully.")