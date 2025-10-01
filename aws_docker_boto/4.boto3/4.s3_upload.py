import boto3

#s3와 연결하기

s3 = boto3.client("s3")

s3.upload_file('./4.boto3/1.intro.py', 'mybucket-sesac24','1.intro.py')
