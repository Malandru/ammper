from rest_framework.request import Request
from rest_framework import status
from api.belvo.consumer import get_belvo_api
from api.belvo.parser import bank_to_dict


class BankingService:
    @staticmethod
    def list_institutions(request: Request):
        belvo_api = get_belvo_api()
        banks = belvo_api.get_institutions()
        response = [bank_to_dict(b) for b in banks]
        return response, status.HTTP_200_OK
