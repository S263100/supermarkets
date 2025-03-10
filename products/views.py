from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Products
from django.contrib.auth.decorators import login_required
from . import forms

from django.shortcuts import render

# Create your views here.
def home(request):
    products = Products.objects.all()
    return render(request, 'home.html', {'products': products})

@login_required(login_url="/users/login/")
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
    if request.method == 'POST':
        form = forms.CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('products:home')
    else:
        form = forms.CreateProduct()
    return render(request, 'products/products_new.html', { 'form': form })
