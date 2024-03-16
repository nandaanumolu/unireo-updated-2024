from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from portal.models.universityinfo import University
from portal.models.univdetail import Univdetail,Univcon
from django.contrib.auth.hashers import make_password,check_password
from django.core.files.storage import FileSystemStorage

class univdetail(View):
    def get(self,request):
        data={}
        print(request.session['Email'])
        university=University.get_university_by_email(request.session['Email'])
        qwe="rty"
        print(university)
        print(qwe)
        if(university):
            univdetail=Univdetail.get_univdetail_by_email(university.Email)
        print(univdetail)
        if(univdetail):
            value={'Type':univdetail.Type,'Name':univdetail.Name,'Year':univdetail.Year,'Rank':univdetail.Rank,
            'Campuses':univdetail.Campuses,'Departments':univdetail.Departments,
            'Email':univdetail.Email,'Web':univdetail.Web,'About':univdetail.About,'Upload':univdetail.Upload}
            data={'value':value}


        return render(request,'BasicInformation.html',data)
        
    def post(self,request):
        Type=request.POST.get('Type')
        Name=request.POST.get('Name')
        Year=request.POST.get('Year')
        Rank=request.POST.get('Rank')
        Campuses=request.POST.get('Campuses')
        Departments = request.POST.get('Departments')
        Email=request.session['Email']
        Web=request.POST.get('Web')
        About=request.POST.get('About')
        print('amar')
        Upload=request.FILES['Upload']
        print("nanda")
        fs=FileSystemStorage()
        name=fs.save(Upload.name,Upload)
        url=fs.url(name)
        print(url)
        if(Email!=request.session['Email']):
            error_message="ohh your email doesn't matched with login mail"
            return render(request,'BasicInformation2.html',{error:error_message})
        else:
            university=University.get_university_by_email(Email)
            print(university.Email)
            univdetail=Univdetail.get_univdetail_by_email(university.Email)
            univdetail1=Univdetail(Type=Type,Name=Name,Year=Year,Rank=Rank,Campuses=Campuses,Departments=Departments,
            Email=Email,Web=Web,About=About,Upload=Upload
            )
            if(univdetail):
                univdetail.delete()
            univdetail1.register()
            value={'Type':Type,'Name':Name,'Year':Year,'Rank':Rank,'Campuses':Campuses,'Departments':Departments,
            'Email':Email,'Web':Web,'About':About,'Upload':url}
            data={'value':value}
            return render(request,'BasicInformation.html',data)
class univcon(View):
    def get(self,request):
        data={}
        university=University.get_university_by_email(request.session['Email'])
        if(university):
            univcon=Univcon.get_univcon_by_email(university.Email)
        if(univcon):
            listreq=[]
            for i in range(0,len(univcon.Req)):
                #print(qwe[i])
                if(univcon.Req[i]=="'"):
                    a=""
                    #print(qwe[i])
                    for j in range(i+1,len(univcon.Req)):
                        #print("nanda")
                        #print(qwe[j])
                        if(univcon.Req[j]=="'" or univcon.Req[j]=="]"):
                            break
                        a=a+univcon.Req[j]
                        #print(a+"kis")
                    if(a!='' and a!=',' and len(a)>3):
                        listreq.append(a)
                    i=j+2
                    #print(j)
            print(listreq)
            print("in order")
            listfea=[]
            for i in range(0,len(univcon.Features)):
                #print(qwe[i])
                if(univcon.Features[i]=="'"):
                    a=""
                    #print(qwe[i])
                    for j in range(i+1,len(univcon.Features)):
                        #print("nanda")
                        #print(qwe[j])
                        if(univcon.Features[j]=="'" or univcon.Features[j]=="]"):
                            break
                        a=a+univcon.Features[j]
                        #print(a+"kis")
                    if(a!='' and a!=',' and len(a)>3):
                        listfea.append(a)
                    i=j+2
                    #print(j)
            print(listfea)
            print("yeah this too")
            value={'Email':univcon.Email,'Intakes':univcon.Intakes,'Award':univcon.Award,'Staff':univcon.Staff,'Students':univcon.Students,
            'Departments':univcon.Departments,
            'Location':univcon.Location,'Link':univcon.Link,'Face':univcon.Face,'Insta':univcon.Insta,'Req':listreq,'Features':listfea,'Video':univcon.Video}
            print(univcon.Req)
            data={'value':value}
            print(value['Intakes'])
        return render(request,'BasicInformation2.html',data)
        
        
    def post(self,request):
        Email=request.session['Email']
        Intakes=request.POST.getlist('Intakes[]')
        print(Intakes)
        Award=request.POST.get('Award')
        Staff=request.POST.get('Staff')
        Students=request.POST.get('Students')
        Departments=request.POST.get('Departments')
        Location=request.POST.get('Location')

        Link=request.POST.get('Link')
        Face=request.POST.get('Face')
        Insta=request.POST.get('Insta')
        Req=request.POST.getlist('Req[]')
        Features=request.POST.getlist('Features[]')
        Video=request.FILES['Video']
        fs=FileSystemStorage()
        name1=fs.save(Video.name,Video)
        url1=fs.url(name1)


        univcon1=Univcon(Email=Email,Intakes=Intakes,Award=Award,Staff=Staff,Students=Students,Departments=Departments,
        Location=Location,Link=Link,Face=Face,Insta=Insta,Req=list(Req),Features=Features,Video=Video
        )

        university=University.get_university_by_email(Email)
        univcon =Univcon.get_univcon_by_email(university.Email)
        if(univcon):
            univcon.delete()
        univcon1.register()
        #Intakes=Intakes
        value={'Email':Email,'Intakes':Intakes,'Award':Award,'Staff':Staff,'Students':Students,'Departments':Departments,
        'Location':Location,'Link':Link,'Face':Face,'Insta':Insta,'Req':Req,'Features':Features,'Video':url1}
        data={'value':value}
        return render(request,'BasicInformation2.html',data)
class univsecurity(View):
    def get(self,request):
        university1=University.get_university_by_email(request.session['Email'])
        print(university1.Phonenumber)
        data={'Phonenumber':university1.Phonenumber}
        return render(request,'Password_security.html',data)
    def post(self,request):
        data={}
        university1=University.get_university_by_email(request.session['Email'])
        Phonenumber=request.POST.get('Phonenumber')
        if(Phonenumber!=None):
            Phonenumber=university1.Phonenumber
            print(university1.Phonenumber)
            university1.register()
        a=university1.Password
        Password=request.POST.get('Password')
        Confirmpassword=request.POST.get('Confirmpassword')
        Confirmpassword1=request.POST.get('Confirmpassword1')
        error_message=None
        flag=check_password(Password,a)
        if(Phonenumber):
            data={'Phonenumber':university1.Phonenumber}
            return render(request,'Password_security.html',data)
        if(flag):
            if(Confirmpassword == Confirmpassword1):

                university1.Password=make_password(Confirmpassword)
                university1.Confirmpassword=make_password(Confirmpassword1)
                university1.register()
                data={'Phonenumber':university1.Phonenumber}
                return render(request,'Password_security.html',data)
            else:
                
                error_message='Password and current password doesnt match !!!'
                data={'Phonenumber':university1.Phonenumber}
                data['error']=error_message

                return render(request,'Password_security.html',data)
        else:
            error_message='Current Password is invalid!!!'
            data={'Phonenumber':university1.Phonenumber}
            data['error']=error_message
            return render(request,'Password_security.html',data)