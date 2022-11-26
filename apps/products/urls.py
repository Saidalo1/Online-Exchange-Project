from django.urls import include, path
from rest_framework.routers import DefaultRouter

from products.views import ProductModelViewSet, ProductImagesViewSet

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')
router.register('product-image', ProductImagesViewSet, 'product-image')

urlpatterns = [
    path('', include(router.urls)),
]
