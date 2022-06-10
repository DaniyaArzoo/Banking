from django.db import models
from profiles.models import Customer

# Create your models here.
class Account(models.Model):
    balance = models.FloatField(default=0.0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id} | {self.customer.name}"


class Transaction(models.Model):
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
