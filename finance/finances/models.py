from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.category.name} - {self.amount}"
