from django.db import models


class Product(models.Model):
    
    name = models.CharField(max_length=100, blank=True, default='abc', verbose_name='名称')
    price = models.IntegerField(default=0, verbose_name='价格')



