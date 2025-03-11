from itertools import product
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



# Create your models here.
class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_id=models.CharField(max_length=64)
    product_name=models.CharField(max_length=64)
    product_price=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    product_stock=models.PositiveIntegerField(default=0)
    product_category=models.CharField(max_length=64, default="")
    product_points=models.PositiveIntegerField(default=0)
    product_description=models.TextField(default="")
    product_image=models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return f"Product_id:{self.product_id},"\
               f"Product_Name:{self.product_name},"\
                f"Product_Price:{self.product_price}" \
               f"Product_Stock:{self.product_stock}" \
               f"Product_Category:{self.product_category}"\
                f"Product_Points:{self.product_points}"\
                f"Product_Description:{self.product_description}"\
                f"Product_Image:{self.product_image}"

class News(models.Model):
    news_title=models.CharField(max_length=100)
    news_date=models.DateTimeField(default=timezone.now)
    news_body=models.TextField(default="")

    def __str__(self):
        return f"News_Title:{self.news_title},"\
                f"News_Date:{self.news_date},"\
               f"News_Body:{self.news_body}"

class Deals(models.Model):
    deal_id = models.CharField(max_length=64)
    deal_product_name = models.CharField(max_length=64)
    deal_original_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    deal_new_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    deal_stock = models.PositiveIntegerField(default=0)
    deal_category = models.CharField(max_length=64, default="")
    deal_points = models.PositiveIntegerField(default=0)
    deal_description = models.TextField(default="")
    deal_image = models.ImageField(default='fallback.png', blank=True)
    deal_image = models.ImageField(default='fallback.png', blank=True)
    is_on_sale = models.BooleanField(default=False)

    def __str__(self):
        return f"Deal_id:{self.deal_id},"\
               f"Deal_Product_Name:{self.deal_product_name},"\
                f"Deal_Original_Price:{self.deal_original_price}" \
               f"Deal_New_Price:{self.deal_new_price}" \
               f"Deal_Stock:{self.deal_stock}" \
               f"Deal_Category:{self.deal_category}"\
                f"Deal_Points:{self.deal_points}"\
                f"Deal_Description:{self.deal_description}"\
                f"Deal_Image:{self.deal_image}"


