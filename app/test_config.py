import os
from dotenv import load_dotenv


def test_load_config():
    load_dotenv('.env')

    assert os.getenv('TEST_API_KEY') is not None
    assert os.getenv('TEST_DB_HOST') is not None

    assert os.getenv('TEST_API_KEY') == 'TestApiKey97531?/'
    assert os.getenv('TEST_DB_HOST') == 'Test_DB_Host97531?/'
