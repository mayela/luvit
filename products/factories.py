from random import randint, uniform
import factory

from .models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    name = factory.Faker('word')
    value = uniform(1.0, 100.0)
    discount_value = uniform(1.0, 100.0)
    stock = randint(1, 100)