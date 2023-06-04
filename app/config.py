import os
from dotenv import load_dotenv
from os import path

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:

    AWS_KEY_ID = os.getenv('AWS_KEY_ID')
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_REGION_NAME = os.getenv('AWS_REGION_NAME')
    AWS_BUCKET = os.getenv('AWS_BUCKET')

    FILE_PATH_INDEX_DATA = 'data/source/indexData.csv'
    FILE_PATH_INDEX_INFO = 'data/source/indexInfo.csv'
    FILE_PATH_INDEX_PROCESSED = 'data/source/indexProcessed.csv'

