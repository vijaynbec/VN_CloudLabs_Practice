import boto3
IAM_client = boto3.client('iam')


# # remove user from group
# IAM_client.remove_user_from_group(
#     GroupName='Boto3',
#     UserName='boto3_user1'
#     )
# # delete group and user if exists
# IAM_client.delete_user(
#     UserName='boto3_user1'
#     )
# IAM_client.delete_group(
#     GroupName='Boto3'
#     )
# #
# # creating new group
IAM_client.create_group(
    GroupName='Boto3'
    )
# creating new user
IAM_client.create_user(
    UserName='boto3_user1'
    )
# creating user to group
IAM_client.add_user_to_group(
    GroupName='Boto3',
    UserName='boto3_user1'
)
IAM_users = IAM_client.list_users()
print(IAM_users)
# listing exisiting users
print('Existing IAM Users and Groups')
for Userlist in IAM_users['Users']:
    print(f'  {Userlist["UserName"]}')
    print({Userlist["UserName"]})

for Userlist in IAM_users['Users']:
    print(f'  {Userlist["UserName"]}')

IAM_Groups = IAM_client.list_groups()
print(IAM_Groups)
for Usergroup in IAM_Groups['Groups']:
    print(f'  {Usergroup["GroupName"]}')


