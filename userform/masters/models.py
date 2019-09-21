from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=50,default='some text')
    jobtitle = models.CharField(max_length=50)
    jobdescription = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Salary(models.Model):
    name = models.CharField(max_length=50,default='some text')
    component_name = models.CharField(max_length=50)
    types = models.CharField(max_length=100)

    # TYPE = (
    #     ('E', 'Earning'),
    #     ('D', 'Deduction'),
    # )
    # types = models.CharField(max_length=1, choices=TYPE)

class Job_category(models.Model):
    name = models.CharField(max_length=50,default='some text')
    jobcategory = models.CharField(max_length=50)
   
class Work_shift(models.Model):
    name = models.CharField(max_length=50,default='some text')
    workshift = models.CharField(max_length=50)
    fro = models.IntegerField()
    to = models.IntegerField()

class Pay_grade(models.Model):
    paygrade = models.CharField(max_length=50,default='some text')
    currency = models.IntegerField()

class Employment_status(models.Model):
    name = models.CharField(max_length=50,default='some text')
    employment_status = models.CharField(max_length=50,default='some text')