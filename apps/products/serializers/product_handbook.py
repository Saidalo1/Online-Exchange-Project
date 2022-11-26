from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from products.models import Category
from products.models import ProductImages


class CategoryModelSerializer(ModelSerializer):
    def validate(self, data):
        if Category.objects.filter(name=data['name']).exists():
            raise ValidationError("This category name is already taken")
        return data

    class Meta:
        model = Category
        exclude = ('slug',)


class ProductImageModelSerializer(ModelSerializer):

    class Meta:
        model = ProductImages
        exclude = ('product',)
