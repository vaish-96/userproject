# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .models import Job,Salary,Job_category,Work_shift,Pay_grade,Employment_status

# Create your views here.
def form(request):
    return render(request,'testapp1/form.html')

def index1(request):
    jobs = Job.objects.all()
    context = {'jobs':jobs}
    return render(request,'testapp1/index1.html',context)

def create(request):
    # print request.POST
    job = Job(name=request.POST['name'],jobtitle=request.POST['jobtitle'],jobdescription=request.POST['jobdescription'])
    job.save()
    return redirect('/master')

def edit(request, id):
    job = Job.objects.get(id=id)
    context = {'job':job}
    return render(request,'testapp1/edit.html',context)

def update(request, id):
    job = Job.objects.get(id=id)
    job.name = request.POST['name']
    job.jobtitle = request.POST['jobtitle']
    job.jobdescription = request.POST['jobdescription']
    job.save()
    return redirect('/master')

def delete(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    return redirect('/master')

################################################################################
# SALARIES                                                                     #
################################################################################

def index_sal(request):
    sals = Salary.objects.all()
    context = {'sals':sals}
    return render(request,'testapp1/test-sal.html',context)

def edit_sal(request, id):
    sal = Salary.objects.get(id=id)
    context = {'sal':sal}
    return render(request,'testapp1/edit-sal.html',context)

def create_sal(request):
    # print request.POST
    sal = Salary(name=request.POST['name'],component_name=request.POST['component_name'],types=request.POST['types'])
    sal.save()
    return redirect('/master/test-sal')

def update_sal(request, id):
    sal = Salary.objects.get(id=id)
    sal.name = request.POST['name']
    sal.component_name = request.POST['component_name']
    sal.types = request.POST['types']
    sal.save()
    return redirect('/master/test-sal')

def delete_sal(request, id):
    sal = Salary.objects.get(id=id)
    sal.delete()
    return redirect('/master/test-sal')

##############################################################################
#                     JOB CATAGORIES                                                       #
##############################################################################    

def index_job(request):
    cats = Job_category.objects.all()
    context = {'cats':cats}
    return render(request,'testapp1/test-job.html',context)

def edit_job(request, id):
    cat = Job_category.objects.get(id=id)
    context = {'cat':cat}
    return render(request,'testapp1/edit-job.html',context)

def create_job(request):
    # print request.POST
    cat = Job_category(name=request.POST['name'],jobcategory=request.POST['jobcategory'])
    cat.save()
    return redirect('/master/test-job')

def update_job(request, id):
    cat = Job_category.objects.get(id=id)
    cat.name = request.POST['name']
    cat.jobcategory = request.POST['jobcategory']
    cat.save()
    return redirect('/master/test-job')

def delete_job(request, id):
    cat = Job_category.objects.get(id=id)
    cat.delete()
    return redirect('/master/test-job')

#############################################################################
#    EMPLOYMENT STATUS                                                      #                                                 #
#############################################################################
def index_status(request):
    statuss = Employment_status.objects.all()
    context = {'statuss':statuss}
    return render(request,'testapp1/test-status.html',context)

def edit_status(request, id):
    status = Employment_status.objects.get(id=id)
    context = {'status':status}
    return render(request,'testapp1/edit-status.html',context)

def create_status(request):
    # print request.POST
    status = Employment_status(name=request.POST['name'],employment_status=request.POST['employment_status'])
    status.save()
    return redirect('/master/test-status')

def update_status(request, id):
    status = Employment_status.objects.get(id=id)
    status.name = request.POST['name']
    status.employment_status = request.POST['employment_status']
    status.save()
    return redirect('/master/test-status')

def delete_status(request, id):
    status = Employment_status.objects.get(id=id)
    status.delete()
    return redirect('/master/test-status')

############################################################################
# WORK SHIFTS                                                                         #
############################################################################

def index_work(request):
    works = Work_shift.objects.all()
    context = {'works':works}
    return render(request,'testapp1/test-work.html',context)

def edit_work(request, id):
    work = Work_shift.objects.get(id=id)
    context = {'work':work}
    return render(request,'testapp1/edit-work.html',context)

def create_work(request):
    work = Work_shift(name=request.POST['name'],
                      workshift=request.POST['workshift'],
                      fro=request.POST['fro'],
                      to=request.POST['to'])
    work.save()
    return redirect('/master/test-work')

def update_work(request, id):
    work  = Work_shift.objects.get(id=id)
    work.name = request.POST['name']
    work.workshift = request.POST['workshift']
    work.fro = request.POST['fro']
    work.to = request.POST['to']
    work.save()
    return redirect('/master/test-work')

def delete_work(request, id):
    work = Work_shift.objects.get(id=id)
    work.delete()
    return redirect('/master/test-work')

############################################################################
# PAY GRADES                                                                         #
############################################################################

def index_pay(request):
    pays = Pay_grade.objects.all()
    context = {'pays':pays}
    return render(request,'testapp1/test-pay.html',context)

def edit_pay(request, id):
    pay = Pay_grade.objects.get(id=id)
    context = {'pay':pay}
    return render(request,'testapp1/edit-pay.html',context)

def create_pay(request):
    # print request.POST
    pay = Pay_grade(paygrade=request.POST['paygrade'],currency=request.POST['currency'])
    pay.save()
    return redirect('/master/test-pay')

def update_pay(request, id):
    pay = Pay_grade.objects.get(id=id)
    pay.paygrade = request.POST['paygrade']
    pay.currency = request.POST['currency']
    pay.save()
    return redirect('/master/test-pay')

def delete_pay(request, id):
    pay = Pay_grade.objects.get(id=id)
    pay.delete()
    return redirect('/master/test-pay')
