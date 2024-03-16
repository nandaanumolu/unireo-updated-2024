from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from portal.models.consultancyinfo import Consultancy
from django.views import View
from django.shortcuts import render,redirect

class agentsignup(View):
    def get(self,request):
        return render(request,'agent_portal/agent_signup.html')
    def post(self,request):
        postData = request.POST
        Firstname=postData.get('Firstname')
        Email=postData.get('Email')
        Phonenumber=postData.get('Phonenumber')
        Password=postData.get('Password')
        Confirmpassword=postData.get('Confirmpassword')
        count=Consultancy.objects.all().count()
        agentid="AGN"+str(count+1)
        
        print(Firstname)

        error_message=None
        agentsignup1=Consultancy.IsExists(Email)
        value={'Firstname':Firstname,'Email':Email,'Password':Password,'Phonenumber':Phonenumber,'Confirmpassword':Confirmpassword}


        print(Email)
        if(agentsignup1):
            error_message="Email already Exists !!"
            data={'value':value , 'error': error_message}
            return render(request,'agent_portal/agent_signup.html',data)
        if(Password !=Confirmpassword ):
            error_message="Password is not valid"
            data={'value':value , 'error': error_message}
            return render(request,'agent_portal/agent_signup.html',data)

        print(Password)

        agentsignup=Consultancy(Firstname =Firstname,Email=Email, Phonenumber= Phonenumber,
        Password=Password,Confirmpassword=Confirmpassword,Agentid=agentid )
        agentsignup.Password=make_password(agentsignup.Password)
        agentsignup.Confirmpassword=make_password(agentsignup.Confirmpassword)
        agentsignup.register()
        print("aaaaaa")
        return redirect('agentloginpage')
