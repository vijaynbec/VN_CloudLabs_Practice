import boto3

s3_resource = boto3.resource('s3')
# create bucket via resource and listing down buckets
s3_resource.create_bucket(Bucket='unique20242005abcvi2024')
all_buckets_resource=s3_resource.buckets.all()
for item in all_buckets_resource:
   print(item)
print(" ------  listing object by resource call")
list_obj=s3_resource.Bucket('unique2024new2005abcvi2024')
for obj in list_obj.objects.all():
    print(obj)
    print(obj.key)


print("********* from client **********")
#
s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket='unique2024new2005abcvi2024')
all_buckets_client=s3_client.list_buckets()
print(all_buckets_client['Buckets'])
print(all_buckets_client['Owner'])
print("********* place object from client call **********")
with open('my_testfile.txt','w') as file:
    file.write('sample_file')
s3_client.upload_file(Filename='my_testfile.txt',
                      Bucket='unique2024new2005abcvi2024',
                      Key='sample_file.txt')


object=(s3_client.get_object(Bucket='unique2024new2005abcvi2024', Key='sample_file.txt' ))
print(object['ContentType'])
#********** Pre signed URL ***********
presign_url = s3_client.generate_presigned_url(ClientMethod='get_object',
                                                Params={'Bucket':'unique2024new2005abcvi2024',
                                                        'Key':'sample_file'},
                                                ExpiresIn=3600,
                                                HttpMethod=None)
print(presign_url)  # sign-in URL

#### Delete Object
s3_client.delete_object(Bucket='unique2024new2005abcvi2024', Key='sample_file.txt')

# delete bucket by s3 resource










#

# first_bucket = s3_resource.Bucket(name='unique20242005abcvi2024')
# first_object = s3_resource.Object(bucket_name='unique20242005abcvi2024', key='first_file_name')
# s3_resource.Object('unique20242005abcvi2024', 'first_file_name').upload_file(
#     Filename='first_file_name')
# # create bucket via client
# s3_client.create_bucket(Bucket='clientunique20242005abcvi2024')
#
#
#
#
#
#
