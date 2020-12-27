import boto3 
from joblib import dump, load
from io import BytesIO

def write_s3(data, bucket, key):

    with BytesIO() as f:
        dump(data, f)
        f.seek(0)
        boto3.client("s3").upload_fileobj(Bucket=bucket, Key=key, Fileobj=f)
        
def read_s3(bucket, key):

    with BytesIO() as f:
        boto3.client("s3").download_fileobj(Bucket=bucket, Key=key, Fileobj=f)
        f.seek(0)
        file = load(f)
    
    return file