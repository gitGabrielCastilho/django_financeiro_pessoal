from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Category, Transaction
from .forms import CategoryForm, TransactionForm, DateFilterForm

def transaction_list(request):
    transactions = Transaction.objects.all()
    total_expenses = transactions.filter(transaction_type='expense').aggregate(total=Sum('amount'))['total'] or 0
    total_income = transactions.filter(transaction_type='income').aggregate(total=Sum('amount'))['total'] or 0
    current_balance = total_income - total_expenses

    if request.method == 'GET':
        form = DateFilterForm(request.GET)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            if start_date:
                transactions = transactions.filter(date__gte=start_date)
            if end_date:
                transactions = transactions.filter(date__lte=end_date)
            total_expenses = transactions.filter(transaction_type='expense').aggregate(total=Sum('amount'))['total'] or 0
            total_income = transactions.filter(transaction_type='income').aggregate(total=Sum('amount'))['total'] or 0
            current_balance = total_income - total_expenses
    else:
        form = DateFilterForm()

    return render(request, 'finances/transaction_list.html', {
        'transactions': transactions,
        'total_expenses': total_expenses,
        'total_income': total_income,
        'current_balance': current_balance,
        'form': form
    })


def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'finances/transaction_form.html', {'form': form})

def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'finances/transaction_form.html', {'form': form})

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'finances/transaction_confirm_delete.html', {'transaction': transaction})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'finances/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'finances/category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'finances/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'finances/category_confirm_delete.html', {'category': category})
