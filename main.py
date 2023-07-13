import pyodbc

from app.get_pandas_df import get_pandas_df
from app.config import Config
from app.database_manager import DatabaseManager
from app.database_load_data import FillTables
from app.database_reader import DatabaseReader
from app.get_pandas_df_from_sql import get_dataframe_from_sql
from app.helpers import get_files_list_from_directory

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
            if table_name == "indexData":
                file_path = Config.FILE_PATH_INDEX_DATA
            elif table_name == "indexInfo":
                file_path = Config.FILE_PATH_INDEX_INFO
            elif table_name == "indexProcessed":
                file_path = Config.FILE_PATH_INDEX_PROCESSED
            # match table_name:
            #     case "indexData":
            #         file_path = Config.FILE_PATH_INDEX_DATA
            #     case "indexInfo":
            #         file_path = Config.FILE_PATH_INDEX_INFO
            #     case "indexProcessed":
            #         file_path = Config.FILE_PATH_INDEX_PROCESSED
            dataframe = get_pandas_df(file_path)
            load_data.fill_table(table_name, dataframe)
        else:
                print(f"Table: {table_name} have data")
except Exception as e:
    print(f"Error in main program with: {e}")


    
try:
    sql_file_task1 = "app/sql_files/task_1.sql"
    sql_file_task2 = "app/sql_files/task_2.sql"
    sql_file_task3 = "app/sql_files/task_3.sql"
    
    dir_path = r'app/sql_files/'
    files_list = get_files_list_from_directory(dir_path)

    for file in files_list:
        sql_file_path = f"{dir_path}{file}"
        df_task = get_dataframe_from_sql(sql_file_path)
        print(df_task)
except pyodbc.Error as e:
    print(f"Error with creating df from sql file: {e} desc:{e}")

