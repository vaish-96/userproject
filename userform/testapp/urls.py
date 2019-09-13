from testapp import views
from django.conf.urls import url

app_name= 'testapp'

urlpatterns =[
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$', views.userlogin,name='login')
]
