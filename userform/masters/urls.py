from django.urls import path
from masters import views

app_name= 'masters'

urlpatterns = [

    path('',views.index1,name='master'),
    path('form/',views.form,name='form'),
<<<<<<< HEAD
=======
#     path('emp/',views.employee,name='employee'),
>>>>>>> d1a5dc5693119cd80b578cde3378f111ca26c033
    path('edit/<id>',views.edit,name='edit'),
    path('create/',views.create,name='create'),
    path('update/<id>',views.update,name='update'),
    path('delete/<id>',views.delete,name='delete'),
    
    path('test-sal/',views.index_sal,name='test-sal'),
    path('edit-sal/<id>',views.edit_sal,name='edit-sal'),
    path('create-sal/',views.create_sal,name='create-sal'),
    path('update-sal/<id>',views.update_sal,name='update-sal'),
    path('delete-sal/<id>',views.delete_sal,name='delete-sal'),

    path('test-job/',views.index_job,name='test-job'),
    path('edit-job/<id>',views.edit_job,name='edit-job'),
    path('create-job/',views.create_job,name='create-job'),
    path('update-job/<id>',views.update_job,name='update-job'),
    path('delete-job/<id>',views.delete_job,name='delete-job'),

    path('test-work/',views.index_work,name='test-work'),
    path('edit-work/<id>',views.edit_work,name='edit-work'),
    path('create-work/',views.create_work,name='create-work'),
    path('update-work/<id>',views.update_work,name='update-work'),
    path('delete-work/<id>',views.delete_work,name='delete-work'),

    path('test-pay/',views.index_pay,name='test-pay'),
    path('edit-pay/<id>',views.edit_pay,name='edit-pay'),
    path('create-pay/',views.create_pay,name='create-pay'),
    path('update-pay/<id>',views.update_pay,name='update-pay'),
    path('delete-pay/<id>',views.delete_pay,name='delete-pay'),

    path('test-status/',views.index_status,name='test-status'),
    path('edit-status/<id>',views.edit_status,name='edit-status'),
    path('create-status/',views.create_status,name='create-status'),
    path('update-status/<id>',views.update_status,name='update-status'),
    path('delete-status/<id>',views.delete_status,name='delete-status'),
    
]
