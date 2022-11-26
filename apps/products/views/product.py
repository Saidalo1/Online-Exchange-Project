from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.order_by('-created_at')
    serializer_class = ProductModelSerializer
    lookup_field = 'slug'
    filter_backends = (DjangoFilterBackend,)
    search_fields = '__all__'
    filterset_fields = {'price': ['gte', 'lte'], 'type_of_price': ['exact'], 'category': ['exact']}
    ordering_fields = '__all__'
