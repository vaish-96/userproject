from django.contrib import admin

# Register your models here.
from per_info_mng.models import Personal_details, Employee_details

# Register your models here.

admin.site.register(Personal_details)
admin.site.register(Employee_details)