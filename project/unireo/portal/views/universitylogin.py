from django.shortcuts import render,redirect,HttpResponseRedirect
import requests,json
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from portal.models.universityinfo import University
from portal.models.univdetail import Univdetail,Univcon
from portal.models.employeeinfo import Employee
#from Portal.models.stddetail import Stddetail
from django.contrib.auth.hashers import check_password
from django.views import View
# Create your views here.

class universitylogin(View):
    return_url = None
    def get(self,request):
        universitylogin.return_url = request.GET.get('return_url')
        return render(request,'signup/New_login.html')

    def post(self,request):
        cap_token=request.POST.get('g-recaptcha-response')
        cap_url="https://www.google.com/recaptcha/api/siteverify"
        cap_secret="6Ldz2mUaAAAAAEdaQk09xE1rimhHzmwCplGIXeqo"
        cap_data={'secret':cap_secret,'response':cap_token}
        cap_server_response=requests.post(url=cap_url,data=cap_data)
        cap_json=json.loads(cap_server_response.text)

        print("vastunda")
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')

        university=University.get_university_by_email(Email)
        if(university):
            print("amartya")
            pass
        else:
            employee1=Employee.get_employee_by_email(Email)
        error_message= None
        if university :
            flag= check_password(Password,university.Password)
            print("hai")
            if flag:
                request.session['Emailemp']=None
                request.session['University']=university.id
                request.session['Firstname']=university.Firstname
                request.session['Email']=university.Email
                request.session['Phonenumber']=university.Phonenumber
                value={'Name':request.session['Firstname']}
                data={'value':value}
                try:
                    univdetail=Univdetail.objects.all().get(Email=university.Email)
                    univcon=Univcon.objects.all().get(Email=university.Email)
                    return render(request,'home_content.html',data)
                except:
                    return redirect('univdetail')

                
                #return render (request,)
                '''
                if Universitylogin.return_url():
                    return HttpResponseRedirect(return_url)
                else:
                    Universitylogin.return_url=None
                    return redirect('homepage')
                    '''
            else:
                error_message='Password is invalid!!!'
        elif employee1:
            if(Password == employee1.Emppassword):
                request.session['Emailemp']=employee1.Empmail
                request.session['Email']=employee1.Univmail
                university=University.get_university_by_email(request.session['Email'])
                request.session['Firstname']=university.Firstname
                request.session['Phonenumber']=university.Phonenumber
                value={'Name':request.session['Firstname']}
                data={'value':value}
                

                return render(request,'home_content.html',data)
            else:
                error_message='Password is invalid!!!' 
        else:
            error_message='Email is invalid!!!'
        return render(request,'signup/New_login.html',{'error':error_message})
def logout(request):

    request.session.clear()
    #print(request.session['Email'])
    return redirect('universityloginpage')
