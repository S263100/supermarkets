
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
path('account/', views.account, name='account'),
    path('support/', views.support, name='support'),
path('news/', views.news, name='news')
]