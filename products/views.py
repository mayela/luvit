import json

from marshmallow import ValidationError

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Product
from .schemas import ProductSchema

def get_all_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        schema = ProductSchema(many=True)
        products_data = schema.dump(products)
        return JsonResponse(data={"products": products_data})

@csrf_exempt
def create_products_bulk(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        products_data = request_data["products"]
        try:
            ProductSchema(many=True).load(products_data)
        except ValidationError as err:
            print(err.messages)
            return JsonResponse(data={
                "status": "OK",
                "products_report": err.messages
                }
            )
        for product in products_data:
            Product.objects.create(**product)
        return JsonResponse(data={"status": "OK"})
