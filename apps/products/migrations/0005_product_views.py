# Generated by Django 4.1.3 on 2022-11-24 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_data_product_specifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.BigIntegerField(default=0),
        ),
    ]
