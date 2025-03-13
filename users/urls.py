from django.template import Template
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import password_change_view, password_change_done_view

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('edit_profile/', views.profile_edit_view, name='edit_profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.profile_view, name='account'),
    path('password/', password_change_view.as_view(), name='password_change'),
    path('password/done/', views.password_change_done_view, name='password_change_done')
]