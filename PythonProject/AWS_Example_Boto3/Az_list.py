import boto3

azs = boto3.client('ec2')
response = azs.describe_availability_zones()

all=response.get('ZoneNames')
print(all)


