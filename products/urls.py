from django.urls import path

from .views import get_all_products, create_products_bulk

urlpatterns = [
    path('', get_all_products),
    path('bulk_insert/', create_products_bulk)
]