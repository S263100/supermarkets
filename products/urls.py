from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),
    path('new-product/', views.product_new, name='new-product'),
    path('users/', include('users.urls')),
    path('account/', views.account, name='account'),
    path('support/', views.support, name='support'),
    path('news/', views.all_news, name='news'),
    path('deals/', views.all_deals, name='deals'),
    path('deal/search/', views.deal_product_search, name='deal_product_search'),
    path('deal/<str:deal_product_name>/', views.deal_product_detail, name='deal_product_detail'),
    path('product/search/', views.product_search, name='product_search'),
    path('product/<str:product_name>/', views.product_detail, name='product_detail'),
    path('new-product/', views.product_new, name='new-product'),
    path('new-news/', views.new_news, name='new-news'),
    path('new-deals/', views.new_deals, name='new-deals')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
