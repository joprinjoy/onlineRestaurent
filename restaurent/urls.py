"""restaurent URL Configuration

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
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('registeruser',views.registerUser),
    path('userreg',views.userReg),
    path('login',views.loginPage),
    path('loginfun',views.loginFun),
    path('addproduct',views.addproduct),
    path('additem',views.additem),
    path('viewmenu',views.vmenu),
    path('addTocart/<int:id>',views.addTocart),
    path('viewcart',views.viewCart),
    path('deleteFromcart/<int:id>',views.deleteFromcart),
    path('viewuser',views.viewUser),
    path('viewitems',views.viewitems),
    path('deleteitem/<int:id>',views.deleteitem),
    path('updateitempage/<int:id>',views.updateitempage),
    path('updateitempage/updateitems/<int:id>',views.updateitems),
    path('checkout',views.checkout),
    path('logoutone',views.logout),


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

