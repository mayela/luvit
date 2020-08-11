from django.shortcuts import render
from django.http import JsonResponse

from .models import Product
from .schemas import ProductSchema

def get_all_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        schema = ProductSchema(many=True)
        products_data = schema.dump(products)
        return JsonResponse(data={"products": products_data})
