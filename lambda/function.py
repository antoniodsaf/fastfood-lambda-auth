import json
import os
import boto3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

cognito = boto3.client('cognito-idp')
cognito_client_id = os.getenv('COGNITO_CLIENT_ID')
cognito_user_pool_id = os.getenv('COGNITO_USER_POOL_ID')
cognito_admin_username = os.getenv('COGNITO_ADMIN_USERNAME')

def sign_up(username):
    try:
        sign_up_response = cognito.sign_up(
            ClientId=cognito_client_id,
            Username=username,
            Password=username
        )
        if sign_up_response['UserConfirmed']:
            return init_auth(username)
        else:
            return None
    except cognito.exceptions.UsernameExistsException as e:
        logger.warning("User ja existente", e)
        return init_auth(username)
    except Exception as e:
        logger.error("Erro ao criar user: %s", e)
        return None

def init_auth(username):
    try:
        return cognito.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': username
            },
            ClientId=cognito_client_id
        )
    except cognito.exceptions.NotAuthorizedException as e:
        logger.warning("User nao autorizado", e)
        return None
    except Exception as e:
        logger.error("Erro ao fazer login: %s", e)
        return None

def handler(event, context):
    try:
        body = json.loads(event['body'])
        username = body.get('cpf', cognito_admin_username)
        
        if not username:
            username = cognito_admin_username
        
        auth_response = sign_up(username)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'User autenticado com sucesso',
                'response': auth_response
            })
        }
    except cognito.exceptions.NotAuthorizedException:
        return {
            'statusCode': 401,
            'body': json.dumps({'message': 'User nao autorizado'})
        }
    except Exception as e:
        logger.error("Erro generico: %s", e)
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Erro generico: ' + str(e)})
        }