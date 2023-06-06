import pyodbc

from config import Config
from my_database import MyDatabase


class DatabaseManager:

    def __init__(self) -> None:
        self.db = MyDatabase()
        self.cursor = self.db.get_connection()

    def is_database_exist(self):
        try:
            sql_exist = f"""SELECT 1 FROM sys.databases WHERE name='{Config.DB_NEW_NAME}'"""
            self.cursor.execute(sql_exist)
            result = self.cursor.fetchone()

            if result[0] is None:
                self.create_database()

        except pyodbc.Error as e:
            print(f"There is a problem with database connection: {e}")
    
    def create_database(self):
        try:
            sql_create = f"""IF NOT EXISTS(SELECT 1 FROM sys.databases WHERE name='{Config.DB_NEW_NAME}')
            CREATE DATABASE {Config.DB_NEW_NAME}""" 
            # USE {Config.DB_NEW_NAME}"""
            print(sql_create)
            self.cursor.execute(sql_create)
        except pyodbc.Error as e:
            print(f"There is a problem with create database: {e}")
        else:
            print("Database created successfully.")

    def is_table_exist(self, table_name):
        try:
            sql_exist = f"""SELECT OBJECT_ID(N'[{Config.DB_NEW_NAME}].[dbo].[{table_name}]', N'U')"""
            self.cursor.execute(sql_exist)
            result = self.cursor.fetchone()

            if result[0] is None:
                self.create_tables(table_name)

        except pyodbc.Error as e:
            print(f"There is a problem with database connection: {e}")

    
    def create_tables(self, table_name):
        try:
            sql_use_db = (
                f"""USE {Config.DB_NEW_NAME}""")
            self.cursor.execute(sql_use_db)

            match table_name:
                case "indexData":
                    sql_create_table = (
                        f"""IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[indexData]') AND type in (N'U'))
                        CREATE TABLE indexData (
                                Id int NOT NULL,
                                IndexText varchar(10) NOT NULL,
                                Date date NOT NULL,
                                OpenCourse NUMERIC(10,6),
                                HighCourse NUMERIC(10,6),
                                LowCourse NUMERIC(10,6),
                                CloseCourse NUMERIC(10,6),
                                Adj_CloseCourse NUMERIC(10,6),
                                Volume int
                                )""")
                    self.cursor.execute(sql_create_table)

                case "indexInfo":
                    sql_create_table = (
                        f"""IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[indexInfo]') AND type in (N'U'))
                        CREATE TABLE indexInfo (
                                Id int NOT NULL,
                                Region varchar(20),
                                Exchange varchar(70),
                                IndexText varchar(15),
                                Currency varchar(10)
                                )""")
                    self.cursor.execute(sql_create_table)

                case "indexProcessed":
                    sql_create_table = (
                        f"""IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[indexProcessed]') AND type in (N'U'))
                        CREATE TABLE indexProcessed (
                                Id int NOT NULL,
                                IndexText varchar(10) NOT NULL,
                                Date date NOT NULL,
                                OpenCourse NUMERIC(10,6),
                                HighCourse NUMERIC(10,6),
                                LowCourse NUMERIC(10,6),
                                CloseCourse NUMERIC(10,6),
                                Adj_CloseCourse NUMERIC(10,6),
                                Volume int,
                                CloseUSDCourse NUMERIC(10,9)
                                )""")		

                    self.cursor.execute(sql_create_table)

        except pyodbc.Error as e:
            print(
                f"There is a problem with create tables {table_name} desc: {e}")
        else:
            print(f"Table {table_name} created successfully.")