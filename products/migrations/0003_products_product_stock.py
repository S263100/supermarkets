# Generated by Django 5.1.6 on 2025-03-06 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
