from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from banking.services import BankingService


# Create your views here.
class BankInstitutions(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (SessionAuthentication, )

    def get(self, request: Request):
        msg, status = BankingService.list_institutions(request)
        return Response(msg, status)
