"""AjCreation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('About-Me/', views.aboutme,name='aboutme'),
    path('About-Us/', views.aboutus,name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('fashion/', views.fashion, name='fashion'),
    path('gallery/', views.gallery, name='gallery'),
    path('night/' , views.night, name='night'),
    path('portrait/', views.portrait, name='portrait'),
    path('pre-babyshoot/',views.prebabyshoot, name="prebabyshoot"),
    path('pre-weddingshoot/',views.preweddingshoot, name='preweddingshoot'),
    path('pricing/',views.Pricingpackage,name='price'),
    path('wedding/', views.wedding, name='wedding')
]
