import boto3

#(1)소스코드로 설정
#session = boto3.Session(profile_name="sesac1")
#s3 = session.client('s3')
#직접 이렇게 코드로 불러오거나
#아니면 환경변수로 불러온후 원래 코드대로 사용
#(2) 환경변수로 설정
# set AWS_PROFILE=sesac1
#s3 = boto3.client('S3')


s3 = boto3.client('s3')

buckets = s3.list_buckets()
print(buckets)
for b in buckets["Buckets"]:
    print(b["Name"])
