import requests
from typing import List
from aws.secret import get_secrets_manager
from api.belvo.endpoints import *
from api.belvo.parser import *

secret_belvo_api = get_secrets_manager().get_secret_belvo_api()
belvo_api = None


class BelvoAPI:
    def __init__(self):
        self.session = requests.session()
        self.session.auth = (secret_belvo_api.api_id, secret_belvo_api.password)

    def get_institutions(self) -> List[Bank]:
        url = get_url(INSTITUTIONS_ENDPOINT)
        payload = self.session.get(url)
        print(payload)
        results: List[Dict] = payload.json().get('results', [])
        return [dict_to_bank(r) for r in results]


def get_url(endpoint):
    return f'{secret_belvo_api.url}{endpoint}'


def get_belvo_api():
    global belvo_api
    if belvo_api is None:
        belvo_api = BelvoAPI()
    return belvo_api
