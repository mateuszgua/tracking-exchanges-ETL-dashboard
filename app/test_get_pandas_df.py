import os
import pandas as pd
import pytest

from dotenv import load_dotenv

from get_pandas_df import get_pandas_df
from config import Config

def test_s3_dataframe():
    expected_columns = ['Index', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj', 'Close', 'Volume']
    load_dotenv('.env')
    file_path = os.getenv('TEST_FILE_ID')
    print(file_path)
    df = get_pandas_df(f"{file_path}")
    print(df)
    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == expected_columns