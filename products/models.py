from django.db import models

'''
Product {
    id: String
    name: String
    value: Float
    discount_value: Float?
    stock: Int
}
'''

class Product(models.Model):
    '''
    Class representing all the fields needed to save the info of a product
    '''
    name = models.CharField(max_length=100)
    value = models.FloatField()
    discount_value = models.FloatField()
    stock = models.IntegerField()
