from typing import List


class FormField:
    def __init__(self, name, validation):
        self.name = name
        self.validation = validation


class Bank:
    def __init__(self, bank_id, name, display_name, link_id, form_fields: List['FormField'], resources: List[str]):
        self.bank_id = bank_id
        self.name = name
        self.display_name = display_name
        self.link_id = link_id
        self.form_fields = form_fields
        self.resources = resources


class Link:
    def __init__(self, link_id, institution):
        self.link_id = link_id
        self.institution = institution


class Account:
    def __init__(self, account_id, link_id, number, name):
        self.account_id = account_id
        self.link_id = link_id
        self.number = number
        self.name = name


class Transaction:
    def __init__(self, trx_id, account, currency, description, value_date, amount, status, trx_type):
        self.trx_id = trx_id
        self.account = account
        self.currency = currency
        self.description = description
        self.value_date = value_date
        self.amount = amount
        self.status = status
        self.trx_type = trx_type


class TransactionBalance:
    def __init__(self, transactions, expenses, incomes):
        self.transactions = transactions
        self.expenses = expenses
        self.incomes = incomes
        self.balance = incomes - expenses
