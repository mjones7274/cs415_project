"""
URL configuration for cs415 project.

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
from cs415 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.user_list),
    path('addresses/', views.address_list),
    path('phones/', views.phone_list),
    path('phone-type/', views.phonetype_list),
    path('address-type/', views.addresstype_list),
    path('user-info/', views.userinfo_list),
    path('pages/', views.pagedata_list),
    path('users/user/<int:id>', views.user),
    path('address/user/<int:id>', views.user_address),
    path('phone/user/<int:id>', views.user_phone),
    path('info/user/<int:id>', views.user_info),
    path('pages/page/<int:id>', views.pagedata),
    path('data/user/<int:id>', views.user_data),
]
