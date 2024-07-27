import json
import boto3
import os

def lambda_handler(event, context):
    ssm_client = boto3.client('ssm')
    s3_client = boto3.client('s3')
    response = ssm_client.get_parameter(Name='/UserName', WithDecryption=False)
    parameter_value = response['Parameter']['Value']
    bucket_name = os.environ['nitindemodxcbucket']
    file_name = 'parameter.txt'
    s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=parameter_value)

    return {
        'statusCode': 200,
        'body': json.dumps('Parameter stored successfully!')
    }
