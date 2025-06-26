# EC2 ID only 
aws ec2 describe-instances \
  --query 'Reservations[].Instances[].InstanceId' \
  --output text | tr '\t' '\n'


# EC2 Name tag only, will print in order to match last step. 



aws ec2 describe-instances \
  --query "Reservations[].Instances[].Tags[?Key=='Name'].Value[]" \
  --output text | tr '\t' '\n'
