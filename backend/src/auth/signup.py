import json
import os
import boto3

client_id = os.environ['clientId']
cognito = boto3.client('cognito-idp')

def signup(event, context):
    body = json.loads(event['body'])
    email = body['email'].lower()
    password = body['password']

    params = {
        'ClientId': client_id,
        'Password': password,
        'Username': email,
        'UserAttributes': [{'Name': 'email', 'Value': email}]
    }

    try:
        result = cognito.sign_up(**params)
        return {
            'statusCode': 200,
            'body': json.dumps(json.dumps({'message': 'Usuario registrado exitosamente'}))
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': str(e)})
        }