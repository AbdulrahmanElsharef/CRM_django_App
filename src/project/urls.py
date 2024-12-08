"""
URL configuration for project project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from CRM_Data import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('dashboard/',views.Orders_Data,name='dashboard'),
    path('Dashboard/',views.Dashboard,name='Dashboard'),
    #Dr_Print
    path('Dr_Print_order_list',views.Dr_Print_order_list,name='Dr_Print_order_list'),
    path('Dr_Print_order_list/<int:id>',views.Dr_Print_invoice,name='Dr_Print_invoice'),
    #Etbaly_Shokran
    path('Etbaly_Shokran_order_list',views.Etbaly_Shokran_order_list,name='Etbaly_Shokran_order_list'),
    path('Etbaly_Shokran_order_list/<int:id>',views.Etbaly_Shokran_invoice,name='Etbaly_Shokran_invoice'),
    # Melouk_Eltibah
    path('Melouk_Eltibah_order_list',views.Melouk_Eltibah_order_list,name='Melouk_Eltibah_order_list'),
    path('Melouk_Eltibah_order_list/<int:id>',views.Melouk_Eltibah_invoice,name='Melouk_Eltibah_invoice'),
    # Print_Square
    path('Print_Square_order_list',views.Print_Square_order_list,name='Print_Square_order_list'),
    path('Print_Square_order_list/<int:id>',views.Print_Square_invoice,name='Print_Square_invoice'),


    ]

#if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
