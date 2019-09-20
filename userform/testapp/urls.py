from testapp import views
from django.urls import path
# from django.contrib.auth.views import 

app_name= 'testapp'

urlpatterns =[
  
    path('register/',views.register,name='register'),
    path('login/', views.userlogin,name='login'),
]
