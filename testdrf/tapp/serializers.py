

from rest_framework import serializers, exceptions

from tapp.models import Product


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['name', 'price']
        
        

