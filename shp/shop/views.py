from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
import math

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    
    params = {'products':products}
    return render(request, 'shop/Index.html', params )

def about(request):
     return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print(name,email,phone,desc)
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def buynow(request):
    return render(request, 'shop/buynow.html')

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")


