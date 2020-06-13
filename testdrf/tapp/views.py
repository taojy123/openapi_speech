from django_filters import rest_framework as filters
from rest_framework import viewsets

from tapp.models import Product
from tapp.serializers import ProductSerializer


class ProductFilter(filters.FilterSet):
    order_by = filters.OrderingFilter(fields=['id', 'username', 'is_active'])

    class Meta:
        model = Product
        fields = {
            'id': ['exact', 'in'],
            'name': ['exact', 'icontains'],
            'price': ['lte', 'gte'],
        }


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    filter_class = ProductFilter
    queryset = Product.objects.order_by('id')

