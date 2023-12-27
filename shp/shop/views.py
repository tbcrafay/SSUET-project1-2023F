from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    params = {'product':products}
    return render(request, 'shop/Index.html', params )

def about(request):
     return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")


