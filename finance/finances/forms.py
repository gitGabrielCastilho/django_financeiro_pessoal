from django import forms
from .models import Transaction
from .models import Category

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'date', 'category', 'transaction_type', 'description']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '$'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/yyyy'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'transaction_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class DateFilterForm(forms.Form):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=False
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=False
    )

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
