from django.urls import path
from banking import views

urlpatterns = [
    path('institutions', views.BankInstitutions.as_view())
]
