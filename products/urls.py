from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),
    path('new-product/', views.product_new, name='new-product'),
    path('users/', include('users.urls')),
    path('account/', views.account, name='account'),
    path('support/', views.support, name='support'),
    path('news/', views.news, name='news'),
    path('deals/', views.deals, name='deals'),
    path('product/search/', views.product_search, name='product_search'),
    path('product/<str:product_name>/', views.product_detail, name='product_detail'),
    path('new-product/', views.product_new, name='new-product')
]

