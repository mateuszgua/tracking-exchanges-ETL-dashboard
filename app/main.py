from get_pandas_df import get_pandas_df
from config import Config
from database_manager import DatabaseManager

db_manager = DatabaseManager()

tables_names = ['indexData', 'indexInfo', 'indexProcessed']

try:
    file_path = Config.FILE_PATH_INDEX_DATA
    df_index_data = get_pandas_df(file_path)

    file_path = Config.FILE_PATH_INDEX_INFO
    df_index_info = get_pandas_df(file_path)

    file_path = Config.FILE_PATH_INDEX_PROCESSED
    df_index_processed = get_pandas_df(file_path)

    db_manager.is_database_exist()

    for table_name in tables_names:
        db_manager.is_table_exist(table_name)
        
except Exception as e:
        print(f"Error in main program with: {e}")