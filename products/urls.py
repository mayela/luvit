from django.urls import path

from .views import get_all_products, create_products_bulk

app_name = 'products'

urlpatterns = [
    path('', get_all_products, name="all-products"),
    path('bulk_insert/', create_products_bulk, name="bulk-insert")
]