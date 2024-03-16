from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from portal.models.stddetail import Stdacd,Stdpro,Stdind,Stdcour,Stdpro1
from portal.models.univdetail import Univdetail,Univcon
from portal.models.consultancyinfo import Consultancy
from portal.models.studentinfo import Student
from portal.models.universityinfo import University
from django.contrib.auth.hashers import make_password,check_password
from portal.models.stddetail import Stdacd,Stdcour,Stdpro,Stdpro1,Stdind
from portal.models.stdappli import Stdappli
from portal.models.coursecommision import Coursecommision
from portal.models.superadmin import Superadmin
from portal.models.courses import Courses
from portal.models.application import Application
from portal.models.addemployee import Addemployee

try:
    a=1
    class adminlogin(View):
        def get(self,request):
            return render(request,'super_admin/adminlogin.html')
        def post(self,request):
            email=request.POST.get('Email')
            password=request.POST.get('Password')
            error=''
            
            try:
                try:
                    admin=Superadmin.objects.get(Email=email)
                    if(admin.Password==password):
                        request.session['adminemail']=email
                        request.session['roleacess']=None
                        return redirect('adminhome')
                    
                except:
                    print("nanda")
                    admin=Addemployee.objects.get(Email=email)
                    print("kishore")
                    if(admin.Password==password):
                        print("mounish")
                        request.session['adminempemail']=email
                        request.session['roleacess']=admin.Roleaccess
                        return redirect('adminhome')
            except:
                error="Email Does Not Exist"
                return render(request,'super_admin/adminlogin.html',{'error':error})


    class addemployee(View):
        def get(self,request):
            return render(request,'super_admin/adminemp.html')
        def post(self,request):
            name=request.POST.get('Name')
            email=request.POST.get('Email')
            phone=request.POST.get('Phonenumber')
            adminmail=request.session['adminemail']
            roleacess=request.POST.get('Roleacess')
            password=request.POST.get('Password')
            confirmpassword=request.POST.get('Confirmpassword')

            employee=Addemployee(Firstname= name, Phonenumber=phone,Roleaccess=roleacess,Adminmail=adminmail,
            Email =email ,Password =password,Confirmpassword =confirmpassword )
            employee.register()
            return render(request,'super_admin/adminemp.html')
            
    def adminlogout(request):
        request.session.clear() 
        return redirect('adminlogin') 

    def Home(request):
        data={}
        data['students']=Student.objects.all().count()
        data['universities']=University.objects.all().count()
        data['agents']=Consultancy.objects.all().count()
        data['totappli']=Stdappli.objects.all().count()
        data['stdappli']=Stdappli.objects.all().filter(agentmail="-").count()
        data['agentappli']=Stdappli.objects.exclude(agentmail='-').count()
        data['accepted']=Stdappli.objects.all().filter(status="accept").count()
        data['rejected']=Stdappli.objects.all().filter(status="reject").count()

        return render(request,'super_admin/home.html',data)
    #def Courses(request):
    #    return render(request,'super_admin/courses.html')
    class Settings(View):
        def get(self,request):
            super1=Superadmin.objects.get(Email=request.session['adminemail'])
            print(super1.Phonenumber)
            data={'Phonenumber':super1.Phonenumber,'Email':super1.Email}
            return render(request,'super_admin/settings.html',data)
            
        def post (self,request):
            data={}
            super1=Superadmin.objects.get(Email=request.session['adminemail'])
            Phonenumber=request.POST.get('Phonenumber')
            if(Phonenumber!=None):
                super1.Phonenumber=Phonenumber
                super1.register()
            print(super1.Phonenumber)
            
            a=super1.Password
            Password=request.POST.get('Password')
            Confirmpassword=request.POST.get('Confirmpassword')
            Confirmpassword1=request.POST.get('Confirmpassword1')
            error_message=None
            flag= (a==Password)
            if(Phonenumber):
                data={'Phonenumber':super1.Phonenumber}
                return render(request,'super_admin/settings.html',data)
            if(flag):
                if(Confirmpassword == Confirmpassword1):

                    super1.Password=Confirmpassword
                    super1.Confirmpassword=Confirmpassword1
                    super1.register()
                    data={'Phonenumber':super1.Phonenumber,'Email':super1.Email}
                    return render(request,'super_admin/settings.html',data)
                else:
                    
                    error_message='Password and confirm password doesnt match !!!'
                    data={'Phonenumber':super1.Phonenumber,'Email':super1.Email}
                    data['error']=error_message

                    return render(request,'super_admin/settings.html',data)
            else:
                error_message='Current Password is invalid!!!'
                data={'Phonenumber':super1.Phonenumber,'Email':super1.Email}
                data['error']=error_message
            return render(request,'super_admin/settings.html',data)
    def students(request):
        stddetail=Stdappli.objects.all()
        data={}
        data['stddetail']=stddetail
        #return render(request,'.html',data)
        return render(request,'super_admin/students.html',data)
    def universities(request):
        university1=University.objects.all()
        data={}
        list=[]
        list1=[]
        name=[]
        phone=[]
        country=[]
        email=[]
        rank=[]
        award=[]
        for i in university1:
            list.extend([[i.Firstname,i.Email]])

        for i in range(0,len(list)):
            name.append(list[i][0])
            email.append(list[i][1])
            phone.append(University.objects.get(Firstname=list[i][0]).Phonenumber)
            country.append(Univcon.objects.get(Email=list[i][1]).Location)
            rank.append(Univdetail.objects.get(Email=list[i][1]).Rank)
            award.append(Univcon.objects.get(Email=list[i][1]).Award)
            #detail[name]={'name':name,'award':award,'country':country,'rank':rank,'email':email,'phone':phone}
        for i in range(0,len(list)):
                    list1.append({'name':name[i],
                            'email':email[i],
                                'phone':phone[i],
                                    'country':country[i],'rank':rank[i],'award':award[i]})    
                                                        
            #print(detail[name])
        data['detail']=list1
        return render(request,'super_admin/universities.html',data)
    def agent(request):
        agent=Consultancy.objects.all()
        data={}
        data['agent']=agent
        return render(request,'super_admin/agents.html',data)
    def single_university(request):
        return render(request,'super_admin/single_university.html')
    def single_agent(request):
        return render(request,'super_admin/single_agent.html')
    class commision(View):
        def get(self,request):
            university=University.objects.all()
            data={}
            data['university']=university        
            return render(request,'super_admin/commision.html',data)
        def post(self,request):
            uniname=request.POST.get('uniname')
            value={}
            data={}
            value['uniname']=uniname
            data['value']=value
            return render(request,'super_admin/commision.html',data)
    class addcommision(View):
        def get(self,request,name="a"):
            university=University.objects.get(Firstname=name)
            print(university.Email)
            courses1=Courses.objects.filter(Email=university.Email)
            print(courses1)
            data={}
            data['courses1']=courses1
            data['uniname']=name
            return render(request,'super_admin/addcommision.html',data)

        def post(self,request,name="a"):
            unimail=University.objects.get(Firstname=name).Email
            name1=request.POST.getlist('name[]')
            curr=request.POST.getlist('curr[]')
            amo=request.POST.getlist('amo[]')
            com=request.POST.getlist('com[]')
            for i in range(0,len(name1)):
                commision=Coursecommision(Uniname=name,Unimail=unimail,Coursename=name1[i],
                Coursecurr=curr[i],Courseamo=amo[i],Coursecomm=com[i])
                commision1=False
                try:
                    commision1=Coursecommision.objects.filter(Unimail=unimail).get(Coursename=name1[i])
                except:
                    pass
                if(commision1):
                    commision1.delete()
                commision.register()
                course1=Courses.objects.filter(Email=unimail).get(Name=name1[i])
                course1.com=com[i]
                course1.register()
            
            courses1=Courses.objects.filter(Email=unimail)
            print(courses1)
            data={}
            data['courses1']=courses1
            data['uniname']=name
            return render(request,'super_admin/addcommision.html',data)
except:
    a=1
    if(a):
        def error(request):
            return redirect('error')


