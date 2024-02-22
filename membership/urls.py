from django.urls import path
from membership import views

urlpatterns = [
    path('register', views.UserRegister.as_view()),
    path('login', views.UserLogin.as_view()),
    path('logout', views.UserLogout.as_view()),
    path('home', views.UserWelcome.as_view()),
]
