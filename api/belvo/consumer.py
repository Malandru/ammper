import requests
from typing import List, Iterable
from aws.secret import get_secrets_manager
from api.belvo.endpoints import Endpoint
from api.belvo.parser import *

secret_belvo_api = get_secrets_manager().get_secret_belvo_api()
belvo_api = None

API_USERNAME = 'banking100'
API_PASSWORD = 'empty'
API_TOKEN = 'abc12345'


class BelvoAPI:
    def __init__(self):
        self.session = requests.session()
        self.session.auth = (secret_belvo_api.api_id, secret_belvo_api.password)

    def get_link(self, bank: Bank) -> Link:
        if bank.link_id is not None:
            return Link(bank.link_id, bank.name)
        url = get_url(Endpoint.LIST_ALL_LINKS)
        for result in get_results_dict(self.session.get(url)):
            link = dict_to_link(result)
            if bank.name == link.institution:
                return link
        # link not found in registered links, so register a link
        url = get_url(Endpoint.REGISTER_LINK)
        body = dict(
            institution=bank.name,
            username=API_USERNAME,
            password=API_PASSWORD,
            external_id='security-testing',
            access_mode='single',
            credentials_storage='5d',
            stale_in='30d',
            fetch_resources=["ACCOUNTS", "OWNERS", "TRANSACTIONS"],
            code=API_TOKEN,
        )
        response = self.session.post(url, json=body).json()
        return dict_to_link(response)

    def get_institutions(self) -> List[Bank]:
        url = get_url(Endpoint.INSTITUTIONS)
        results = get_results_dict(self.session.get(url))
        return [dict_to_bank(r) for r in results]

    def retrieve_accounts(self, bank: Bank) -> Iterable[Account]:
        link = self.get_link(bank)
        url = get_url(Endpoint.RETRIEVE_ACCOUNTS)
        body = dict(
            link=link.link_id,
            token=API_TOKEN,
            save_data=True,
        )
        results = self.session.post(url, json=body).json()
        return map(dict_to_account, results)

    def retrieve_transactions(self, request_data: Dict) -> Iterable[Transaction]:
        extra = dict(
            token=API_TOKEN,
            save_data=True,
        )
        url = get_url(Endpoint.RETRIEVE_TRANSACTIONS)
        body = request_data | extra
        results = self.session.post(url, json=body).json()
        return map(dict_to_transaction, results)


def get_url(endpoint):
    return f'{secret_belvo_api.url}{endpoint}'


def get_results_dict(payload) -> List[Dict]:
    return payload.json().get('results', [])


def get_belvo_api():
    global belvo_api
    if belvo_api is None:
        belvo_api = BelvoAPI()
    return belvo_api
