import sys


libnames = ['boto3', 'time', 'botocore']
for libname in libnames:
    try:
        lib = __import__(libname)
    except:
        print(sys.exc_info())
    else:
        globals()[libname] = lib


    try:
        s3 = boto3.resource('s3')
    except:
        print(sys.exc_info())

# response = s3.list_buckets()

gbl_project_base="s3test"

gbl_project_name = gbl_project_base + '-' + str(int(time.time()))


print("setting epoch to: %s" % int(time.time()))
print("Project name: %s" % gbl_project_name)

# s3 = boto3.resource('s3')
# gbl_project_name = 'some-private-bucket'
# gbl_project_name = 'bucket-to-check'

bucket = s3.Bucket(gbl_project_name)


def check_bucket(bucket):
    try:
        s3.meta.client.head_bucket(Bucket=gbl_project_name)
        print("Bucket Exists!")
        return True
    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            print("Bucket Does Not Exist!")
            return False

print("checking for bucket: %s" % check_bucket(bucket))



# Get a list of all bucket names from the response
# buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
# print("Bucket List: %s" % buckets)



# result = s3.get_bucket_acl(Bucket='nathgibb-scripts')
# print(result)

# s3.create_bucket(Bucket='571589702451-0001-bucket')

# response = s3.create_bucket(
#    ACL='private',
#    Bucket='571589702451-0001-ngpythontest'
# )

# response = client.create_bucket(
#    ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
#    Bucket='string',
#    CreateBucketConfiguration={
#        'LocationConstraint': 'EU'|'eu-west-1'|'us-west-1'|'us-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1'|'cn-north-1'|'eu-central-1'
#    },
#    GrantFullControl='string',
#    GrantRead='string',
#    GrantReadACP='string',
#    GrantWrite='string',
#    GrantWriteACP='string'
# )
