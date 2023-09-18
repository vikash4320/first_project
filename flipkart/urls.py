"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)


urlpatterns = [
    
    path('',views.index,name='home'),
    path('sign',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logot',views.logout,name='logout'),
    path('cart',views.cart_details,name='cart'),
    path('checkout', views.check_cart, name="checkout"),
    path('order', views.order_details, name="order"),
    path('api', include(router.urls)),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)