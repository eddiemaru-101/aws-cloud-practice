import boto3

sts = boto3.client('sts')
id = sts.get_caller_identity()
print(id)


