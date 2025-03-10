from django import forms
from . import models

class CreateProduct(forms.ModelForm):
    class Meta:
        model = models.Products
        fields = ['product_id','product_name','product_price','product_stock',
                  'product_category','product_points','product_description',
                  'product_image']