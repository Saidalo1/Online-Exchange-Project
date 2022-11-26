from django.db.models import CASCADE, Model, ForeignKey, ImageField
from django.utils.text import slugify
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from apps.shared.django import SlugBaseModel


class Category(SlugBaseModel, MPTTModel):
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += Category.objects.filter(slug=self.slug).count()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class MPTTMeta:
        order_insertion_by = ['name']


class ProductImages(Model):
    product = ForeignKey('products.Product', CASCADE, 'product_images')
    image = ImageField(upload_to='products/images/')
