import pandas as pd

from get_s3_object import get_object_from_s3

def get_pandas_df(file_path):
    try:
        s3_object = get_object_from_s3(file_path)
        data = s3_object['Body']
        df_pandas = pd.read_csv(data) 
    except Exception as e:
        print(f"Error with created pandas dataframe: {e}")
    else:
        return df_pandas
    