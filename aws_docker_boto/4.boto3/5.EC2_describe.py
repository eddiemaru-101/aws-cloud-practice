import boto3

# EC2 클라이언트 생성 (서울 리전)
ec2 = boto3.client('ec2', region_name='ap-northeast-2')

# 제어할 인스턴스 ID
instance_id = "i-0d2222770a4c3289a"

# 인스턴스 상태 확인
status = ec2.describe_instances(InstanceIds=[instance_id])
state = status['Reservations'][0]['Instances'][0]['State']['Name']
print(f"현재 상태: {state}")

# 인스턴스 중지
ec2.stop_instances(InstanceIds=[instance_id])
print(f"{instance_id} 중지 요청 완료")

# 인스턴스 재시작
ec2.start_instances(InstanceIds=[instance_id])
print(f"{instance_id} 재시작 요청 완료")
