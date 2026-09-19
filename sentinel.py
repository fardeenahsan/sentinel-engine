import boto3
BUCKET_NAME = 'cloud-sentinel-2026-fardeenahsan'
s3= boto3.client('s3')
try:
    response=s3.list_objects_v2(Bucket=BUCKET_NAME)
    if 'Contents' in response:
        print(f"Bucket {BUCKET_NAME} contains:")
        for obj in response['Contents']:
            print(f"-{obj['Key']}")
    else:
        print(f"Bucket{BUCKET_NAME} is empty.")
except Exception as e:
        print(f"Error; {e}")
