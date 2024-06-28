from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from django.template import loader
import datetime
import ecommapp.forms as employeemodule
from ecommapp.models import Employee,FileFactory
from django.shortcuts import render,redirect

def home(request):
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

def index(request):
    template = loader.get_template('index.html')  # getting our template
    name = {
        'employee': 'Dinesh'
    }
    return HttpResponse(template.render(name))

# @require_http_methods(["GET"])
# def show(request):
#     return HttpResponse('<h1>This is Http GET request.</h1>')

def employee(request):
    if request.method == "POST":
        form = employeemodule.EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        employee = employeemodule.EmployeeForm()
        return render(request,"employee.html",{'form':employee})

def show(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = employeemodule.EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")


def fetchData(request,path):
    _instance=FileFactory.choose(path)
    return HttpResponse(_instance.parsed_data())

