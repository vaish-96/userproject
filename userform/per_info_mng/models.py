from django.db import models
# Create your models here.

class Personal_details(models.Model):

    first_name = models.CharField(max_length=150,null = True)
    middle_name = models.CharField(max_length=150,blank = False)
    last_name = models.CharField(max_length=150,blank = False)
    employee_id = models.IntegerField(blank = False)
    date_of_birth = models.DateTimeField(blank = False)
    marital_status = models.SmallIntegerField(default=1,blank = False)
    gender = models.SmallIntegerField(default=1,blank = False)
    nationality = models.SmallIntegerField(default=1,blank = False)
    nick_name = models.CharField(max_length=150,blank = True)
    aadhar_card_no = models.BigIntegerField(blank = False)

    def __str__(self):
       return self.first_name

class Employee_details(models.Model):

   joined_date = models.DateField(blank = False)
   date_of_permanency = models.DateField(blank = False) 
   job_title = models.BigIntegerField(default=1,blank = False)
   employement_status = models.BigIntegerField(default=1,blank = False)
   job_category = models.BigIntegerField(default=1,blank = False)
   work_shifts = models.IntegerField(default=1,blank = False)

# class Employee_table(models.Model):

   #  emp_id = models.IntegerField(blank = False)
   #  first_name = models.CharField(max_length=150,null = True)
   #  job_title = models.BigIntegerField(default=1,blank = False)
   #  employement_status = models.BigIntegerField(default=1,blank = False)
   #  nationality = models.SmallIntegerField(default=1,blank = False)
