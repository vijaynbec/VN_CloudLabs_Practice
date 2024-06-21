import boto3
s3c = boto3.client('s3')
s3c.create_bucket(Bucket='abcd-xyz-test20240529')


response = s3c.list_buckets()
print(response)


# Output the bucket names
print('Existing buckets:')
for items in response['Buckets']:
    print(f'  {items["Name"]}')

all=response.get('Buckets')
print(all)

IAM = boto3.client('iam')
response = IAM.list_users()
print('Existing IAM Users')
for Userlist in response['Users']:
    print(f'  {Userlist["UserName"]}')
print('Existing IAM UserIds')
for UserIds in response['Users']:
    print(f'  {UserIds["UserId"]}')
print('Existing IAM Arns')
for UserArn in response['Users']:
    print(f'  {UserArn["Arn"]}')





