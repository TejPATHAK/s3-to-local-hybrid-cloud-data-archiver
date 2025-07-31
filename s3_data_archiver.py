import boto3
import os

s3 = boto3.client('s3')

bucket_name = 'live-data-storing-place'
local_archive_path = os.path.expanduser('~/archive-data')

print(f"Checking files in bucket: {bucket_name}")
response = s3.list_objects_v2(Bucket=bucket_name)

if 'Contents' not in response:
    print(" No files found in the S3 bucket.")
else:
    for obj in response['Contents']:
        key = obj['Key']
        local_file_path = os.path.join(local_archive_path, key)

        print(f" Processing: {key}")
        if not os.path.exists(local_file_path):
            print(f"⬇ Downloading {key} to {local_file_path}")
            s3.download_file(bucket_name, key, local_file_path)
            print(f" Deleting {key} from S3...")
            s3.delete_object(Bucket=bucket_name, Key=key)
        else:
            print(f"Already archived: {key}")

