from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from membership.services import MembershipService


# Create your views here.
class UserRegister(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request: Request):
        msg, status = MembershipService.create_user(request)
        return Response(msg, status)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny, )
    authentication_classes = (SessionAuthentication, )

    def post(self, request: Request):
        msg, status = MembershipService.check_user(request)
        return Response(msg, status)


class UserWelcome(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (SessionAuthentication, )

    def get(self, request: Request):
        msg, status = MembershipService.welcome()
        return Response(msg, status)

"""
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            print(form.data.get('password'))
            hashed_password = make_password(form.data.get('password'))
            sign_up = form.save(commit=False)
            sign_up.password = hashed_password
            sign_up.save()
            return HttpResponse('OK')
    return HttpResponseBadRequest('NOT OK')
"""
