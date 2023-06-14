import pandas as pd
import pyodbc

from get_pandas_df import get_pandas_df
from config import Config
from database_manager import DatabaseManager
from database_load_data import FillTables
from database_reader import DatabaseReader


db_manager = DatabaseManager()

tables_names = ['indexData', 'indexInfo', 'indexProcessed']

try:            

    db_manager.is_database_exist()

    for table_name in tables_names:
        db_manager.is_table_exist(table_name)
    
    db_reader = DatabaseReader()
    
    for table_name in tables_names:
        table_is_empty = db_reader.is_empty(table_name)
        
        if table_is_empty is True:
            load_data = FillTables()
            match table_name:
                case "indexData":
                    file_path = Config.FILE_PATH_INDEX_DATA
                case "indexInfo":
                    file_path = Config.FILE_PATH_INDEX_INFO
                case "indexProcessed":
                    file_path = Config.FILE_PATH_INDEX_PROCESSED
            dataframe = get_pandas_df(file_path)
            load_data.fill_table(table_name, dataframe)
        else:
                print(f"Table: {table_name} have data")
except Exception as e:
    print(f"Error in main program with: {e}")

def get_dataframe_from_sql(sql_file_path):
    try:
        # db_manager = MyDatabase()
        sql_file = open(sql_file_path)
        sql_as_string = sql_file.read()
        result = db_reader.sql_get_all(sql_as_string)
        result_df = pd.DataFrame(result)
    except pyodbc.Error as e:
        print(e)
        return f"Error: {e}"
    finally:
        sql_file.close()
        return result_df
    
try:
    sql_file_task1 = "app/sql_files/task_1.sql"
    df_task1 = get_dataframe_from_sql(sql_file_task1)
    print(df_task1)
except pyodbc.Error as e:
    print(e)

