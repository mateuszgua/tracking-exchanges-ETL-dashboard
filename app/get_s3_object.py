from s3_manager import get_s3_client
from config import Config


def get_object_from_s3(file_path):
    try:
        s3 = get_s3_client()
        s3_object = s3.get_object(Bucket=Config.AWS_BUCKET,
                            Key=file_path)
    except Exception as e:
        print(f"Error with get list from s3 bucket: {e}")
        print(f"Path: {file_path}")
    else:
        return s3_object