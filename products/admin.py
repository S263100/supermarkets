from django.contrib import admin
from .models import Products, News, Deals

# Register your models here.
admin.site.register(Products)

class ProductsAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(News)
admin.site.register(Deals)