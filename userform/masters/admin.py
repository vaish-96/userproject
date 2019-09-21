# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from masters.models import Job,Salary,Job_category,Work_shift,Pay_grade,Employment_status

# Register your models here.

admin.site.register(Job)
admin.site.register(Salary)
admin.site.register(Job_category)
admin.site.register(Work_shift)
admin.site.register(Pay_grade)
admin.site.register(Employment_status)