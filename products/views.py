from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Products, Deals
from .models import News
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.models import User, Group

from . import forms

from django.shortcuts import render

# Create your views here.
def home(request):
    products = Products.objects.all()
    is_admin = request.user.groups.filter(name="Admin").exists()
    return render(request, 'home.html', {'products': products, 'is_admin': is_admin})

@login_required(login_url="/users/login/")
def account(request):
    is_admin = request.user.groups.filter(name="Admins").exists()
    return render(request, 'account.html'), {'is_admin': is_admin}

def support(request):
    return render(request, 'support.html')

def news(request):
    is_admin = request.user.groups.filter(name="Admin").exists()
    return render(request, 'news.html', {'is_admin': is_admin})

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

def all_news(request):
    news_list = News.objects.all().order_by('news_date')
    is_admin = request.user.groups.filter(name="Admin").exists()
    return render(request, 'news.html', {'news_list': news_list, 'is_admin': is_admin})

def all_deals(request):
    deals_list = Deals.objects.all()
    is_admin = request.user.groups.filter(name="Admin").exists()
    return render(request, 'deals.html', {'deals_list': deals_list, 'is_admin': is_admin})

def deal_product_detail(request, deal_product_name):
    deal = get_object_or_404(Deals, deal_product_name=deal_product_name, is_on_sale=True)
    is_admin = request.user.groups.filter(name="Admin").exists()
    return render(request, 'deal_product_detail.html', {'deal': deal, 'is_admin': is_admin})


def deal_product_search(request):
    query = request.GET.get('q', '')
    if query:
        deals_list = Deals.objects.filter(Q(deal_product_name__icontains=query) | Q(deal_category__icontains=query))
    else:
        deals_list = Deals.objects.all()

    is_admin = request.user.groups.filter(name="Admin").exists()
    return render(request, 'deal_product_search.html', {'deals_list': deals_list, 'query': query, 'is_admin': is_admin})

@permission_required("products.new-product", login_url="/login", raise_exception=True)
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

@permission_required("products.new-news", login_url="/login", raise_exception=True)
@login_required(login_url="/users/login/")
def new_news(request):
    if request.method == 'POST':
        form = forms.CreateNews(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.user = request.user
            news.save()
            return redirect('products:news')
    else:
        form = forms.CreateNews()
    return render(request, 'new_news.html', { 'form': form })

@permission_required("products.new-deals", login_url="/login", raise_exception=True)
@login_required(login_url="/users/login/")
def new_deals(request):
    if request.method == 'POST':
        form = forms.CreateNews(request.POST, request.FILES)
        if form.is_valid():
            deals = form.save(commit=False)
            deals.user = request.user
            deals.save()
            return redirect('products:deals')
    else:
        form = forms.CreateDeals()
    return render(request, 'new_deals.html', { 'form': form })