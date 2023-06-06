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