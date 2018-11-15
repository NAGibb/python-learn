
import sys

libnames = ['boto3']
for libname in libnames:
    try:
        lib = __import__(libname)
    except:
        print(sys.exc_info())
    else:
        globals()[libname] = lib

    try:
        client = boto3.client('apigateway', region_name='us-east-1')
    except:
        print(sys.exc_info())


# response = client.create_rest_api(
#     name='string',
#     description='string',
#     version='string',
#     cloneFrom='string',
#     binaryMediaTypes=[
#         'string',
#     ],
#     minimumCompressionSize=123,
#     apiKeySource='HEADER' | 'AUTHORIZER',
#     endpointConfiguration={
#         'types': [
#             'REGIONAL' | 'EDGE' | 'PRIVATE',
#         ]
#     },
#     policy='string'
# )
    try:
        response = client.create_rest_api(name='gway_test')
        print(response)
    except:
        print(sys.exc_info())
