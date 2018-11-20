# this script is meant to run from an instance whose role has permissions
# to use aws services. Running this script outside of this context may result
# in unpredictable behavior.

import sys, time

# project base name - used to build out s3 folder structure and tagging
prj_base_name = "olivaw"

# project increment name - uses with basename to create unique folders
# unix epoch by default
#prj_inc_name = str(int(time.time()))

# testing only
prj_inc_name = "1542654814"



# project name is base name + increment name
prj_name = prj_base_name + '-' + prj_inc_name

print("Project name: %s" % prj_name)


# import libraries we need
libnames = ['boto3', 'botocore']

# import what we need
for libname in libnames:
    try:
        lib = __import__(libname)
    except:
        print(sys.exc_info())
    else:
        globals()[libname] = lib

# start functions
#
# check to see if bucket exists
# returns true / false
def bucket_exists(bucket_exists_bucket_name):
    try:
        bucket_exists_s3 = boto3.resource('s3')
    except:
        print(sys.exc_info())

    try:
        bucket_exists_s3.meta.client.head_bucket(Bucket=bucket_exists_bucket_name)
        return True
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            return False
# create bucket
# returns true / false
def create_bucket(create_bucket_name):
    try:
        create_bucket_s3 = boto3.resource('s3')
    except:
        print(sys.exc_info())

    try:
        create_bucket_status = create_bucket_s3.create_bucket(Bucket=create_bucket_name)
        return True
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            return False

# create the bucket layout
# returns true / false
def create_bucket_layout(create_bucket_layout_bucket_name):
    try:
        create_bucket_layout_bucket_exists = bucket_exists(create_bucket_layout_bucket_name)
    except:
        print(sys.exc_info())
        return False

    try:
        create_bucket_layout_s3 = boto3.resource('s3')
    except:
        print(sys.exc_info())
        return False

    #if no bucket exists create the parent bucket:
    if create_bucket_layout_bucket_exists is False:
        try:
            create_bucket_layout_parent_status = create_bucket(create_bucket_layout_bucket_name)
            #print("bucket layout parent status: %s" % create_bucket_layout_parent_status)
        except:
            print(sys.exc_info())
            return False

        #create child folders under parent bucket:
        if create_bucket_layout_parent_status is True:
            create_bucket_layout_folders  = ['control-jobs', 'control-archive', 'output-logs', 'output-companies']
            for child_bucket in create_bucket_layout_folders:
                try:
                    create_bucket_folder(create_bucket_layout_bucket_name, child_bucket)
                    #create_folder = create_bucket_layout_s3.put_object(Bucket=create_bucket_layout_bucket_name, Key=child_bucket +'/')
                    #print (create_folder)
                    # create_bucket(create_bucket_layout_bucket_name/child_bucket)
                except:
                    print(sys.exc_info())
                    return False


def create_bucket_folder(create_bucket_bucket_name, create_bucket_folder_name):
    try:
        create_bucket_folder_s3 = boto3.client('s3')
    except:
        print(sys.exc_info())
        return False

    try:
        response = create_bucket_folder_s3.put_object(Bucket=create_bucket_bucket_name, Key=create_bucket_folder_name + '/')
        return True
    except:
        print(sys.exc_info())
        return False


#import boto3
#import logging
#s3_client = boto3.client('s3')






#
#
# End functions



bucket_layout_status = create_bucket_layout(prj_name)
#print (bucket_layout_status)
#
