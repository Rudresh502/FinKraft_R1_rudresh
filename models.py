from django.db import models

class Transaction(models.Model):
    TransactionID = models.CharField(max_length=100)
    CustomerName = models.CharField(max_length=100)
    TransactionDate = models.DateField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Status = models.CharField(max_length=100)
    InvoiceURL = models.URLField()
