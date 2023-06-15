import pandas as pd
import pyodbc

from database_reader import DatabaseReader

def get_dataframe_from_sql(sql_file_path):
    try:
        db_reader = DatabaseReader()
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