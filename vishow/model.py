from django.db import models

class Stock(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2)
    # ... other fields
