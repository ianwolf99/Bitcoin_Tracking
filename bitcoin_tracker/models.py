# Create your models here.
from django.db import models

class BitcoinPrice(models.Model):
    date = models.DateField()
    price = models.FloatField()

    def __str__(self):
        return f"Date: {self.date}, Price: {self.price}"
