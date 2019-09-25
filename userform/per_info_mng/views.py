from django.shortcuts import render,redirect
from .models import Personal_details, Employee_details
# , Employee_table
# Create your views here.

def Personal_details_view(request):
    if request.method =="POST":
        personal = Personal_details(first_name=request.POST['first_name'],
                                middle_name=request.POST['middle_name'],
                                last_name =request.POST['last_name'],
                                employee_id=request.POST['employee_id'],
                                date_of_birth=request.POST['date_of_birth'],
                                marital_status=request.POST['marital_status'],
                                gender=request.POST['gender'],
                                nationality=request.POST['nationality'],
                                nick_name=request.POST['nick_name'],
                                aadhar_card_no=request.POST['aadhar_card_no'])
        personal.save()
        return redirect('/index/text')
    else:
        return render(request,'testapp2/base.html',{})


def Employee_details_view(request):
    if request.method =="POST":
        employee = Employee_details(joined_date=request.POST['joined_date'],
                                date_of_permanency=request.POST['date_of_permanency'],
                                job_title =request.POST['job_title'],
                                employement_status=request.POST['employement_status'],
                                job_category=request.POST['job_category'],
                                work_shifts=request.POST['work_shifts'])
        employee.save()
        return redirect('/index/')
    else:
        return render(request,'testapp2/text.html',{})


def index(request):
    personals = Personal_details.objects.all()
    employees = Employee_details.objects.all()

    # context1 = {'personals':personals}
    # context2 = {'employees':employees}
    # mylist = zip(context1,context2)
    # context = {'mylist':mylist}
    return render(request,'testapp2/index.html',{'personals':personals,
                                                 'employees':employees})

def create(request):
    # print request.POST
    personal = Personal_details(employee_id=request.POST['employee_id'],
                        first_name=request.POST['first_name'],
                        nationality=request.POST['nationality'])
                       
    # employee = Employee_details(employement_status=request.POST['employement_status'],
                                # job_title=request.POST['job_title'])

    personal.save()
    # employee.save()
    return redirect('/index/')

def edit(request, id):
    personal = Personal_details.objects.get(id=id)
    # employee = Employee_details.objects.get(id=id)
    context = {'personal':personal}
    return render(request,'testapp2/edit.html',context)

def update(request, id):
    personal = Personal_details.objects.get(id=id)
    # employee = Employee_details.objects.get(id=id)
    personal.employee_id = request.POST['employee_id']
    personal.first_name = request.POST['first_name']
    personal.nationality = request.POST['nationality']
    # employee.employement_status = request.POST['employement_status']
    # employee.job_title = request.POST['job_title']

    personal.save()
    # employee.save()
    return redirect('/index/')

def delete(request, id):
    personal = Personal_details.objects.get(id=id)
    # employee = Employee_details.objects.get(id=id)
    personal.delete()
    # employee.delete()
    return redirect('/index/')