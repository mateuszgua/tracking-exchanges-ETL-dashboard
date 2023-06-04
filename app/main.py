from get_pandas_df import get_pandas_df
from config import Config

try:
    file_path = Config.FILE_PATH_INDEX_DATA
    df_index_data = get_pandas_df(file_path)

    file_path = Config.FILE_PATH_INDEX_INFO
    df_index_info = get_pandas_df(file_path)

    file_path = Config.FILE_PATH_INDEX_PROCESSED
    df_index_processed = get_pandas_df(file_path)

except Exception as e:
        print(f"Error with: {e}")