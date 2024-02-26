from api.belvo.interfaces import Bank, Link, Account, Transaction, TransactionBalance, FormField
from typing import Dict


def form_field_to_dict(form_field: FormField):
    return dict(
        name=form_field.name,
        validation=form_field.validation,
    )


def dict_to_form_field(body: Dict):
    return FormField(
        name=body.get('name'),
        validation=body.get('validation')
    )


def bank_to_dict(bank: Bank):
    form_fields = map(form_field_to_dict, bank.form_fields)
    return dict(
        bank_id=bank.bank_id,
        name=bank.name,
        display_name=bank.display_name,
        link_id=bank.link_id,
        form_fields=form_fields,
        resources=bank.resources,
    )


def dict_to_bank(body: Dict) -> Bank:
    bank_id = body.get('id')
    form_fields = map(dict_to_form_field, body.get('form_fields'))
    return Bank(
        bank_id=bank_id if bank_id else body.get('bank_id'),
        name=body.get('name'),
        display_name=body.get('display_name'),
        link_id=body.get('link_id', None),
        form_fields=list(form_fields),
        resources=body.get('resources', [])
    )


def link_to_dict(link: Link):
    return dict(
        link_id=link.link_id,
        bank_name=link.institution,
    )


def dict_to_link(body: Dict) -> Link:
    return Link(
        link_id=body.get('id'),
        institution=body.get('institution')
    )


def dict_to_account(body: Dict) -> Account:
    return Account(
        account_id=body.get('id'),
        link_id=body.get('link'),
        number=body.get('number'),
        name=body.get('name'),
    )


def account_to_dict(account: Account) -> Dict:
    return dict(
        account_id=account.account_id,
        link_id=account.link_id,
        account_name=account.name,
        account_number=account.number,
    )


def dict_to_transaction(body: Dict) -> Transaction:
    account = dict_to_account(body.get('account'))
    return Transaction(
        trx_id=body.get('id'),
        account=account,
        currency=body.get('currency'),
        description=body.get('description'),
        value_date=body.get('value_date'),
        amount=body.get('amount'),
        status=body.get('status'),
        trx_type=body.get('type')
    )


def transaction_to_dict(transaction: Transaction) -> Dict:
    return dict(
        trx_id=transaction.trx_id,
        account=transaction.account.account_id,
        currency=transaction.currency,
        description=transaction.description,
        value_date=transaction.value_date,
        amount=transaction.amount,
        status=transaction.status,
        trx_type=transaction.trx_type,
    )


def balance_to_dict(transaction_balance: TransactionBalance) -> Dict:
    return dict(
        incomes=transaction_balance.incomes,
        expenses=transaction_balance.expenses,
        balance=transaction_balance.balance,
        transactions=map(transaction_to_dict, transaction_balance.transactions),
    )
