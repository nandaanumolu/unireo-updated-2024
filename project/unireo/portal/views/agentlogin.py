from django.shortcuts import render,redirect,HttpResponseRedirect
import requests,json
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from portal.models.consultancyinfo import Consultancy
#from Portal.models.stddetail import Stddetail
from django.contrib.auth.hashers import check_password
from django.views import View
# Create your views here.
class agentlogin(View):
    #print("ento batuku")
    return_url = None
    def get(self,request):
        agentlogin.return_url = request.GET.get('return_url')
        return render(request,'agent_portal/agent_login.html')

    def post(self,request):
        cap_token=request.POST.get('g-recaptcha-response')
        cap_url="https://www.google.com/recaptcha/api/siteverify"
        cap_secret="6Ldz2mUaAAAAAEdaQk09xE1rimhHzmwCplGIXeqo"
        cap_data={'secret':cap_secret,'response':cap_token}
        cap_server_response=requests.post(url=cap_url,data=cap_data)
        cap_json=json.loads(cap_server_response.text)
        #if(cap_json['success']==False):
        #    error_message='Captcha is invalid!! Try Again Pls!'
        #    return render(request,'agent_portal/agent_login.html',{'error':error_message})

        print("vastunda")
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        agent=Consultancy.get_consultancy_by_email(Email)
        error_message= None
        if agent:
            print("nanda")
            flag= check_password(Password,agent.Password)
            print("hai")
            if flag:
                print("sjkefsfnecurngfhrdgfjsnrhfvjdfghncjgh")
                request.session['agentid']=agent.Agentid
                request.session['Firstname2']=agent.Firstname
                request.session['Email2']=agent.Email
                request.session['Phonenumber2']=agent.Phonenumber
                value={'Name':request.session['Firstname2']}
                data={'value':value}
                return render(request,'agent_portal/index.html',data)
                #return render (request,)
                '''
                if Universitylogin.return_url():
                    return HttpResponseRedirect(return_url)
                else:
                    Universitylogin.return_url=None
                    return redirect('homepage')
                    '''
            else:
                print("sdjiuerhgiuhre")
                error_message='Password is invalid!!!'
        else:
            error_message='Email is invalid!!!'
        return render(request,'agent_portal/agent_login.html',{'error':error_message})
def logout(request):

    request.session.clear()
    #print(request.session['Email'])
    return redirect('agentloginpage')
