from django import forms
from . import models

class CreateProduct(forms.ModelForm):
    class Meta:
        model = models.Products
        fields = ['product_id','product_name','product_price','product_stock',
                  'product_category','product_points','product_description',
                  'product_image']

class CreateNews(forms.ModelForm):
    class Meta:
        model = models.News
        fields = ['news_title','news_body']

class CreateDeals(forms.ModelForm):
    class Meta:
        model = models.Deals
        fields = ['deal_id', 'deal_product_name','deal_original_price','deal_new_price','deal_category',
                  'deal_points', 'deal_description','deal_image']

