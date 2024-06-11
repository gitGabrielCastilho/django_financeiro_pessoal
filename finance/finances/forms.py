from django import forms
from .models import Transaction
from .models import Category

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'date', 'category', 'transaction_type', 'description']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
