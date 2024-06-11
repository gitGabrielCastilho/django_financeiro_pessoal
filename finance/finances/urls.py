from django.urls import path
from .views import (
    transaction_list, transaction_create, transaction_update, transaction_delete,
    category_list, category_create, category_update, category_delete
)

urlpatterns = [
    path('', transaction_list, name='transaction_list'),
    path('new/', transaction_create, name='transaction_create'),
    path('edit/<int:pk>/', transaction_update, name='transaction_update'),
    path('delete/<int:pk>/', transaction_delete, name='transaction_delete'),
    path('categories/', category_list, name='category_list'),
    path('categories/new/', category_create, name='category_create'),
    path('categories/edit/<int:pk>/', category_update, name='category_update'),
    path('categories/delete/<int:pk>/', category_delete, name='category_delete'),
]
