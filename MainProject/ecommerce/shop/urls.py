"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from shop import views
app_name='shop'
urlpatterns = [
    path('',views.CategoryView.as_view(),name='categoryview'),
    path('more/<int:i>', views.MoreView.as_view(), name='moreview'),
    path('details/<int:i>', views.ProductDetailView.as_view(), name='productdetails'),
    path('login', views.LoginView.as_view(), name='usrlogin'),
    path('register' , views.RegisterView.as_view(), name='usrregister'),
    path('usrlogout', views.LogoutView.as_view(), name='usrlogout'),
    path('addcategories', views.AddCategoryView.as_view(), name='addcategories'),
    path('addproducts', views.AddProductsView.as_view(), name='addproducts'),

]
