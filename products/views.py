from django.shortcuts import render
from django.db.models import Q
from .models import Products

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