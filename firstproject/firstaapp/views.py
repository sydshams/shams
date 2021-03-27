from django.shortcuts import render
from firstaapp.models import Employee


# Create your views here.
def wish(request):

    return render(request,'firstaapp/index.html')
def empview(request):
    emp_list=Employee.objects.all()
    my_dict={"emp_list":emp_list}
    return render(request,'firstaapp/index.html',context=my_dict)
