from itertools import product

from django.db import models

# Create your models here.
class Products(models.Model):
    objects = product
    product_id=models.CharField(max_length=64)
    product_name=models.CharField(max_length=64)
    product_price=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    product_stock=models.PositiveIntegerField(default=0)
    product_category=models.CharField(max_length=64, default="")
    product_points=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Product_id:{self.product_id},"\
               f"Product_Name:{self.product_name},"\
                f"Product_Price:{self.product_price}" \
               f"Product_Stock:{self.product_stock}" \
               f"Product_Category:{self.product_category}"\
                f"Product_Points:{self.product_category}"



