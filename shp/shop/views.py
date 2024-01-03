from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
import math
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    
    # for the filter system:
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    room_number = request.GET.get('room_number')
    flat_number = request.GET.get('flat_number')

    # Fetch available price ranges
    max_price_options = Product.objects.values_list('price', flat=True).distinct()

    if min_price and max_price:
        products = products.filter(price__gte=min_price, price__lte=max_price)
    if room_number:
        products = products.filter(room_number=room_number)
    if flat_number:
        products = products.filter(flat_number=flat_number)

    # Handle empty results and display messages
    if not products:
        # Display appropriate messa
        ...
        
    params = {'products': products, 'max_price_options': max_price_options}

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

def buynow(request, product_id=None):
    products = Product.objects.all()

    if product_id:
        selected_product = get_object_or_404(Product, id=product_id)
        context = {'product': selected_product}
    else:
        context = {'products': products}

    return render(request, 'shop/buynow.html', context)





def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")


