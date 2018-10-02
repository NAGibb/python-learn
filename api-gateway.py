import boto3


client = boto3.client('apigateway', region_name='us-east-1')


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
response = client.create_rest_api(
     name='gway_test'
 )
print(response)
