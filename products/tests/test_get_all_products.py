import json

import pytest

from django.urls import reverse

from products.factories import ProductFactory
from products.models import Product

@pytest.mark.django_db
def test_get_all_products():
    ProductFactory.create_batch(5)
    expected = 5
    assert expected == Product.objects.all().count()

@pytest.mark.django_db
def test_get_all_products_ok(client):
    url = reverse('products:all-products')
    response = client.get(url)
    raw_data = response.content
    data = json.loads(raw_data)
    assert response.status_code == 200
    assert 'products' in data
