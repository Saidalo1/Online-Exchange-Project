from ckeditor.fields import RichTextField
from django.db.models import DecimalField, ForeignKey, CASCADE, JSONField, SET_NULL, CharField, TextChoices, \
    BigIntegerField

from apps.shared.django import SlugBaseModel, TimeBaseModel


class Product(SlugBaseModel, TimeBaseModel):
    class PriceType(TextChoices):
        sum = 'sum'
        dollar = 'y.e'

    description = RichTextField()
    price = DecimalField(decimal_places=2, max_digits=12)
    type_of_price = CharField(max_length=3, choices=PriceType.choices)
    category = ForeignKey('products.Category', CASCADE)
    specifications = JSONField(default=dict)
    views = BigIntegerField(default=0)
    updated_by = ForeignKey('users.User', SET_NULL, null=True, blank=True)
    created_by = ForeignKey('users.User', CASCADE, 'products')

    def save(self, *args, **kwargs):
        while Product.objects.filter(slug=self.slug).exists():
            self.slug += f'{Product.objects.filter(slug=self.slug).count()}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
