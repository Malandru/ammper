from django.urls import path
from banking import views

urlpatterns = [
    path('institutions', views.BankInstitutions.as_view()),
    path('accounts', views.BankAccounts.as_view()),
    path('transactions', views.AccountTransactions.as_view())
]
