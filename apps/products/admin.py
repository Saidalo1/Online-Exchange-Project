from django.contrib import admin
from django.contrib.admin import ModelAdmin

from products.models import Product, Category


# Register your models here.

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    exclude = ('updated_by', 'slug',)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    exclude = ('slug',)
