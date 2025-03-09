from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Products
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

# Create your views here.
def home(request):
    products = Products.objects.all()
    return render(request, 'home.html', {'products': products})

def account(request):
    return render(request, 'account.html')

def support(request):
    return render(request, 'support.html')

def news(request):
    return render(request, 'news.html')

def deals(request):
    return render(request, 'deals.html')

def product_search(request):
    query = request.GET.get('q', '')
    if query:
        products = Products.objects.filter(Q(product_name__icontains=query)| Q(product_category__icontains=query))
    else:
        products = Products.objects.all()

    return render(request, 'product_search.html', {'products': products, 'query': query})

def product_detail(request, product_name):
    product = get_object_or_404(Products, product_name=product_name)
    return render(request, 'product_detail.html', {'product': product})

@login_required(login_url="/users/login/")
def product_new(request):
    return render(request, 'products/products_new.html')