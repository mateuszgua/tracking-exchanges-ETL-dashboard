import boto3
from botocore.exceptions import ClientError

from config import Config

def get_s3_client():
    config = Config()
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=config.AWS_KEY_ID,
            aws_secret_access_key=config.AWS_ACCESS_KEY,
            region_name=config.AWS_REGION_NAME
        )
    except ClientError as e:
        return f"Error with create s3 bucket connection: {e}"
    else:
        return s3
