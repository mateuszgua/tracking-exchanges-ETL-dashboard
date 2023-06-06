import os
import boto3
import pytest


from dotenv import load_dotenv

@pytest.fixture(scope='session')
def s3_client():
    return boto3.client('s3')

@pytest.fixture(scope='session')
def test_bucket_name():
    load_dotenv('.env')
    bucket_name = os.getenv('AWS_BUCKET')
    if not bucket_name:
        pytest.skip("S3_BUCKET_NAME environment variable not set")
    return bucket_name

def test_s3_get_object(s3_client, test_bucket_name):
    load_dotenv('.env')
    object_key = os.getenv('TEST_FILE_ID')
    response = s3_client.get_object(Bucket=test_bucket_name, Key=object_key)
    assert response['ResponseMetadata'][
        'HTTPStatusCode'] == 200, f"Failed to get S3 object: {response}"