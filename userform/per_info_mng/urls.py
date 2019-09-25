from django.urls import path
from per_info_mng import views

app_name ='per_info_mng'

urlpatterns =[
    path('info/',views.Personal_details_view,name = 'info'),
    path('text/',views.Employee_details_view,name = 'text'),
    path('delete/<id>',views.delete,name='delete'),
    path('update/<id>',views.update,name='update'),
    path('edit/<id>',views.edit,name='edit'),
    path('',views.index,name = 'index'),

]
