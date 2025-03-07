from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
path('account/', views.account, name='account'),
    path('support/', views.support, name='support'),
path('news/', views.news, name='news'),
    path('deals/', views.deals, name='deals'),
    path('product/search/', views.product_search, name='product_search'),
path('product/<str:product_name>/', views.product_detail, name='product_detail'),
]
