from django.contrib import admin
from django.urls import path

from ecommerce.models import registeration
from. import views

urlpatterns = [
    path('home/',views.index, name = 'home'),
    path('contact/',views.contact , name= 'contact'),
    path('signup/',views.signup , name = 'signup'),
    path('login_info/',views.login_info, name="login_info"),
    path('cart/',views.cart, name ='cart' ),
    path('checkout/', views.checkout, name = "checkout"),
    path('logout/',views.logout, name = 'logout'),
    path('ordersdtls/',views.ordersdtls,name='ordersdtls')
]
