from rest_framework.viewsets import ModelViewSet

from products.models import ProductImages
from products.serializers import ProductImageModelSerializer


class ProductImagesViewSet(ModelViewSet):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImageModelSerializer

    def list(self, request, *args, **kwargs):
        queryset = ProductImages.objects.filter(slug=kwargs['slug'])
        return super().list(request, *args, **kwargs)
