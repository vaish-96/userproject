"""usermodform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from per_info_mng import views
from masters import views
from django.urls import path, include
from django.contrib import admin
from testapp import views

urlpatterns = [

   path('admin/', admin.site.urls),
   path('master/',include('masters.urls')),
   path('test/', include('testapp.urls')),
   path('index/',include('per_info_mng.urls')),
   path('logout/',views.userlogout,name='logout'),
   path('', views.index),
   
]
