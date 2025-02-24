from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def account(request):
    return render(request, 'account.html')