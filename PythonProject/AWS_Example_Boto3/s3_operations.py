import boto3
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
    print(f'  {bucket["CreationDate"]}')

client = boto3.client('iam')
response = client.list_users()
print('Existing IAM Users')
for Userlist in response['Users']:
    print(f'  {Userlist["UserName"]}')
print('Existing IAM UserIds')
for UserIds in response['Users']:
    print(f'  {UserIds["UserId"]}')
print('Existing IAM Arns')
for UserArn in response['Users']:
    print(f'  {UserIds["Arn"]}')

