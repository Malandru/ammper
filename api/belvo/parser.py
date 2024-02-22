from api.belvo.interfaces import Bank
from typing import Dict


def bank_to_dict(bank: Bank):
    return dict(
        bank_id=bank.bank_id,
        name=bank.name,
        display_name=bank.display_name,
    )


def dict_to_bank(body: Dict) -> Bank:
    return Bank(
        body.get('id'),
        body.get('name'),
        body.get('display_name')
    )
