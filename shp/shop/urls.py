
from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path("", views.index, name="Shop Home"),
    path('about/', views.about,name="AboutUs"),
    path('contact/', views.contact,name="ContactUs"),
    path('tracker', views.tracker,name="TrackingStatus"),
    path('buynow/', views.buynow, name="buynow_root"),
    path('buynow/<int:product_id>/', views.buynow, name="buynow"),
    path('productview/', views.productView,name="Tracking"), 
    path('checkout/', views.checkout,name="Checkout"),   
    
]