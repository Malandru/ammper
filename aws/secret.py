import json
import boto3
from botocore.exceptions import ClientError
from typing import List
from aws.constants import *

secrets_manager = None


class SecretsManager:
    def __init__(self):
        session = boto3.session.Session()
        self.client = session.client(service_name=AWS_SECRET_SERVICE, region_name=AWS_REGION)
        self.secret = self.__get_secret__(AWS_SECRET_NAME)

    def __get_secret__(self, secret_name) -> dict:
        try:
            get_secret_value_response = self.client.get_secret_value(SecretId=secret_name)
        except ClientError as e:
            # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
            raise e
        secret_string = get_secret_value_response['SecretString']
        return json.loads(secret_string)

    def split_field(self, field, separator=','):
        field_str = str(self.secret.get(field))
        return field_str.split(separator)

    def get_secret_database(self):
        return SecretDatabase(self.secret)

    def get_allowed_origins(self) -> List[str]:
        return self.split_field('allowed_origins')

    def get_allowed_hosts(self) -> List[str]:
        return self.split_field('allowed_hosts')

    def get_secret_belvo_api(self):
        return SecretBelvoAPI(self.secret)


class SecretDatabase:
    def __init__(self, secret: dict):
        self.username = secret.get('username')
        self.password = secret.get('password')
        self.hostname = secret.get('hostname')
        self.port = secret.get('port')
        self.database = secret.get('database')


class SecretBelvoAPI:
    def __init__(self, secret: dict):
        self.url = 'https://sandbox.belvo.com'
        self.api_id = secret.get('belvo_id')
        self.password = secret.get('belvo_password')


def get_secrets_manager() -> SecretsManager:
    global secrets_manager
    if secrets_manager is None:
        secrets_manager = SecretsManager()
    return secrets_manager
