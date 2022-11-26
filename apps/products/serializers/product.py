from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from products.models import Product
from products.serializers.product_handbook import ProductImageModelSerializer, CategoryModelSerializer


class ProductModelSerializer(ModelSerializer):
    created_by = HiddenField(default=CurrentUserDefault())
    updated_by = HiddenField(default=CurrentUserDefault())

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['images'] = ProductImageModelSerializer(instance.product_images.first()).data
        represent['category'] = CategoryModelSerializer(instance.category).data
        return represent

    def validate(self, attrs):
        # wota serializer tekwiraman
        return super().validate(attrs)

    class Meta:
        model = Product
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        exclude = ('slug',)
