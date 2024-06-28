from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from django.template import loader
import datetime
import ecommapp.forms as employeemodule
from ecommapp.forms import HLMForm
from ecommapp.models import Employee,FileFactory,VEmployee,PermanentEmployee
from django.shortcuts import render,redirect


def showForm(request,level):
    # if request.method == "POST":
    #     form = employeemodule.EmployeeForm(request.POST)
    #     if form.is_valid():
    #         try:
    #             form.save()
    #             return redirect('/show')
    #         except:
    #             pass
    # else:

    instance=PermanentEmployee(level).payment()
    frmName=str(type(instance).__name__)+"Form"
    print(frmName)
    print(getattr(employeemodule,frmName))
    return render(request,"employee.html")