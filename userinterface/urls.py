"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.UserSignup, name='Signup'),
    path('login/',views.UserLoginpage, name='Login'),
    path('logout/',views.UserLogout, name='Logout'),
    path('product-view/<int:myid>',views.ProductView, name="Product View"),
    path('product-search/',views.Productsearch, name="search"),
    path('product-search/product-view/<int:myid>',views.ProductView, name="search"),
    path('cheackout/',views.ProductCheckout, name="search"),
    path('tracker/',views.ProductTracker, name="Track Order"),
    path('detailscheck/',views.DetailCheck, name="Check Details"),
    path('cheackout/paymenthandler/', views.paymenthandler, name='paymenthandler'),
]
