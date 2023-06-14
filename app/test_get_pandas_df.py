import os
import pandas as pd

from dotenv import load_dotenv

from get_pandas_df import get_pandas_df

from config import Config

def test_s3_dataframe():
    expected_columns = ['Index', 'DateExch', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    load_dotenv('.env')
    Config.AWS_BUCKET = os.getenv('AWS_BUCKET')
    file_path = os.getenv('TEST_FILE_ID')

    df = get_pandas_df(file_path)
    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == expected_columns