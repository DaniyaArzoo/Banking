from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=32)
    phone_no = models.PositiveBigIntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
