import boto3
ec2_resource = boto3.resource('ec2') #, region_name = 'us-wast-1')

create_instances = ec2_resource.create_instances(
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    ImageId="ami-0bb84b8ffd87024d8"  # lookup in the console
)

print(list(ec2_resource.instances.all()))
# ec2_client = boto3.client('ec2')
# del_instances = ec2_client.terminate_instances(InstanceIds=[ec2_resource.instances.all()])

