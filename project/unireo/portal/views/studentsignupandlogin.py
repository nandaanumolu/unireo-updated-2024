from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from portal.models.studentinfo import Student
from portal.models.stddetail import Stdacd,Stdcour,Stdpro,Stdpro1,Stdind
from django.views import View
import requests,json
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class studentsignup(View):
    def get(self,request):
        return render(request,'signup/new_student_signup.html')
    def post(self,request):
        postData = request.POST
        Firstname=postData.get('Firstname')
        Email=postData.get('Email')
        Phonenumber=postData.get('Phonenumber')
        Password=postData.get('Password')
        Confirmpassword=postData.get('Confirmpassword')
        print(Firstname)

        error_message=None
        studentsignup1=Student.IsExists(Email)
        value={'Firstname':Firstname,'Email':Email,'Password':Password,'Phonenumber':Phonenumber,'Confirmpassword':Confirmpassword}


        print(Email)
        if(studentsignup1):
            error_message="Email already Exists !!"
            data={'value':value , 'error': error_message}
            return render(request,'signup/new_student_signup.html',data)
        if(Password !=Confirmpassword ):
            error_message="Password is not valid"
            data={'value':value , 'error': error_message}
            return render(request,'signup/new_student_signup.html',data)

        print(Password)

        studentsignup=Student(Firstname =Firstname,Email=Email,Phonenumber=Phonenumber,
        Password=Password,Confirmpassword=Confirmpassword )
        studentsignup.Password=make_password(studentsignup.Password)
        studentsignup.Confirmpassword=make_password(studentsignup.Confirmpassword)
        studentsignup.register()
        print("aaaaaa")
        return redirect('studentloginpage')
class studentlogin(View):
    #print("ento batuku")
    return_url = None
    def get(self,request):
        studentlogin.return_url = request.GET.get('return_url')
        return render(request,'signup/New_studentlogin.html')

    def post(self,request):
        cap_token=request.POST.get('g-recaptcha-response')
        cap_url="https://www.google.com/recaptcha/api/siteverify"
        cap_secret="6Ldz2mUaAAAAAEdaQk09xE1rimhHzmwCplGIXeqo"
        cap_data={'secret':cap_secret,'response':cap_token}
        cap_server_response=requests.post(url=cap_url,data=cap_data)
        cap_json=json.loads(cap_server_response.text)
        #if(cap_json['success']==False):
        #    error_message='Captcha is invalid!! Try Again Pls!'
        #    return render(request,'signup/New_studentlogin.html',{'error':error_message})

        print("vastunda")
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        student=Student.get_student_by_email(Email)
        error_message= None
        if student :
            flag= check_password(Password,student.Password)
            print("hai")
            if flag:
                request.session['Student']=student.id
                request.session['Firstname1']=student.Firstname
                request.session['Email1']=student.Email
                value={'Name':request.session['Firstname1']}
                data={'value':value}
                try:
                    stdacd=Stdacd.objects.all().get(Email=student.Email)
                    stdind=Stdind.objects.all().get(Email=student.Email)
                    stdcour=Stdcour.objects.all().get(Email=student.Email)
                    return render(request,'student_portal/index.html',data)
                except:
                    return redirect('stdind')
                
                #return render (request,)
                '''
                if studentlogin.return_url():
                    return HttpResponseRedirect(return_url)
                else:
                    studentlogin.return_url=None
                    return redirect('homepage')
                    '''
            else:
                error_message='Password is invalid!!!'
        else:
            print(Email)
            error_message='Email is invalid!!!'
        return render(request,'signup/New_studentlogin.html',{'error':error_message})
def logout1(request):

    users=User.objects.all().filter(email=request.session['Email1'])
    
    if(users):
        for user in range(1,len(users)):
            users[user].delete()
        request.session.clear()
        return redirect('/logout1')
    print(users)
    request.session.clear()
    #print(request.session['Email'])

    return redirect('studentloginpage')

