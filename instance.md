aws configure
aws sts get-caller-identity 
aws ec2 describe-intances

aws ec2 describe-instances \
    --query "Reservations[*].Instances[*].{ID:InstanceId, Name:Tags[?Key=='Name']|[0].Value, PublicIP:PublicIpAddress, PrivateIP:PrivateIpAddress}" \
    --output table



aws ec2 run-instances \
  --image-id ami-0a12345bcdef \
  --count 1 \
  --instance-type t2.micro \
  --key-name MyKeyPair \
  --security-group-ids sg-0123abcd4567efgh \
  --subnet-id subnet-0abc123de456fghij \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=MyNewInstance}]'



aws ec2 run-instances \
    --image-id <AMI_ID> \
    --count 1 \
    --instance-type <INSTANCE_TYPE> \
    --key-name <KEY_PAIR_NAME> \
    --security-group-ids <SG_ID> \
    --subnet-id <SUBNET_ID> \
    --user-data file://<SCRIPT_FILE_PATH> \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=<INSTANCE_NAME>}]'
