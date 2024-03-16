from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from portal.models.universityinfo import University
from django.views import View
from django.shortcuts import render,redirect
class universitysignup(View):
    def get(self,request):
        return render(request,'signup/new_university_signup.html')
    def post(self,request):
        postData = request.POST
        Firstname=postData.get('Firstname')
        Email=postData.get('Email')
        Phonenumber=postData.get('Phonenumber')
        Password=postData.get('Password')
        Confirmpassword=postData.get('Confirmpassword')
        print(Firstname)

        error_message=None
        universitysignup1=University.IsExists(Email)
        value={'Firstname':Firstname,'Email':Email,'Password':Password,'Phonenumber':Phonenumber,'Confirmpassword':Confirmpassword}


        print(Email)
        if(universitysignup1):
            error_message="Email already Exists !!"
            data={'value':value , 'error': error_message}
            return render(request,'signup/new_university_signup.html',data)
        if(Password !=Confirmpassword ):
            error_message="Password is not valid"
            data={'value':value , 'error': error_message}
            return render(request,'signup/new_university_signup.html',data)

        print(Password)

        universitysignup=University(Firstname =Firstname,Email=Email,Phonenumber=Phonenumber,
        Password=Password,Confirmpassword=Confirmpassword )
        universitysignup.Password=make_password(universitysignup.Password)
        universitysignup.Confirmpassword=make_password(universitysignup.Confirmpassword)
        universitysignup.register()
        print("aaaaaa")
        return redirect('universityloginpage')
