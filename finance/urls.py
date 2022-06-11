from django.urls import path
from finance import views

urlpatterns = [
    path("payment/", views.transfer_money, name="payment"),
    path("passbook/", views.passbook, name="passbook"),
]
