from rest_framework.request import Request
from rest_framework import status
from api.belvo.consumer import get_belvo_api
from api.belvo.parser import bank_to_dict, dict_to_bank, account_to_dict, balance_to_dict
from api.belvo.interfaces import TransactionBalance

belvo_api = get_belvo_api()


class BankingService:
    @staticmethod
    def list_institutions(request: Request):
        banks = belvo_api.get_institutions()
        response = [bank_to_dict(b) for b in banks]
        return response, status.HTTP_200_OK

    @staticmethod
    def list_accounts(request: Request):
        bank = dict_to_bank(request.data)
        accounts = belvo_api.retrieve_accounts(bank)
        response = map(account_to_dict, accounts)
        return response, status.HTTP_200_OK

    @staticmethod
    def list_transactions(request: Request):
        transactions = list(belvo_api.retrieve_transactions(request.data))
        incomes, expenses = 0, 0
        for transaction in transactions:
            if transaction.status != 'PROCESSED':
                continue
            if transaction.trx_type == 'OUTFLOW':
                expenses += transaction.amount
            elif transaction.trx_type == 'INFLOW':
                incomes += transaction.amount
            else:
                print(transaction.trx_type)
        balance = TransactionBalance(transactions, incomes=incomes, expenses=expenses)
        response = balance_to_dict(balance)
        return response, status.HTTP_200_OK

