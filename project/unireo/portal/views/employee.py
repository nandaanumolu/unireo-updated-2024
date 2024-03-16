from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from portal.models.universityinfo import University
from portal.models.univdetail import Univdetail,Univcon
from portal.models.employeeinfo import Employee

class Empdeatails(View):
    def get(self,request):
        return render(request,'Addemployee.html')
    def post(self,request):
        Empname=request.POST.get('Empname')
        Empdesg=request.POST.get('Empdesg')
        Empphone=request.POST.get('Empphone')
        Empmail=request.POST.get('Empmail')
        Emppassword=request.POST.get('Emppassword')
        Empconfirmpassword=request.POST.get('Empconfirmpassword')
        Univmail=request.session['Email']
        Employee1=Employee(Empname=Empname,Empdesg=Empdesg,Empphone=Empphone,Empmail=Empmail,Emppassword=Emppassword,
                           Empconfirmpassword=Empconfirmpassword,Univmail=Univmail )
        Employee1.register()
        return render(request,'Addemployee.html')
def Allemp(request):
    employee1=Employee.objects.all().filter(Univmail=request.session['Email'])
    print(employee1)
    return render(request,'Allemployee.html',{'employee1':employee1})