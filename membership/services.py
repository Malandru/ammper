from typing import Tuple
from rest_framework.request import Request
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from membership.forms import RegisterForm


class MembershipService:
    @staticmethod
    def create_user(request: Request) -> Tuple[str, int]:
        form = RegisterForm(data=request.POST)
        if not form.is_valid():
            return form.errors.as_text(), status.HTTP_400_BAD_REQUEST
        hashed_password = make_password(form.data.get('password'))
        user: User = form.save(commit=False)
        user.password = hashed_password
        user.save()
        return "User created", status.HTTP_201_CREATED

    @staticmethod
    def check_user(request: Request):
        username = request.data['username']
        plain_password = request.data['password'].strip()
        user = authenticate(username=username, password=plain_password)
        if not user:
            return "user not authenticated", status.HTTP_401_UNAUTHORIZED
        login(request, user)
        return "welcome", status.HTTP_200_OK

    @staticmethod
    def drop_session(request: Request):
        logout(request)
        return "good bye", status.HTTP_200_OK

    @staticmethod
    def welcome():
        return "only for registered users", status.HTTP_200_OK
