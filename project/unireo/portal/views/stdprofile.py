from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from django.core.files.storage import FileSystemStorage
from portal.models.stddetail import Stdacd,Stdpro,Stdind,Stdcour,Stdpro1
from portal.models.univdetail import Univdetail,Univcon
from portal.models.studentinfo import Student
from portal.models.universityinfo import University
from django.contrib.auth.hashers import make_password,check_password
from portal.models.stddetail import Stdacd,Stdcour,Stdpro,Stdpro1,Stdind
from portal.models.stdappli import Stdappli
from portal.models.courses import Courses
from portal.models.application import Application
from django.contrib.auth.models import User

from datetime import datetime


from portal.models.saved import Saved

class stdind(View):
    def get(self,request):
        data={}
        print(request.session['Email1'])
        student=Student.get_student_by_email(request.session['Email1'])
        qwe="rty"
        print(student)
        print(qwe)
        if(student):
            stdind=Stdind.get_stdind_by_email(student.Email)
        print(stdind)
        if(stdind):
            value={'Firstname': stdind.Firstname,'Lastname': stdind.Lastname,'Dateofbirth':stdind.Dateofbirth,'Gender':stdind.Gender,
                'Maritial':stdind.Maritial,'Nationality':stdind.Nationality,'Email' : stdind.Email,'Address':stdind.Address,'City':stdind.City,'State':stdind.State,
                'Country':stdind.Country,'Phonenumber': stdind.Phonenumber}
            data={'value':value}

        return render(request,'student_portal/Personal_details.html',data)
    def post(self,request):
        print("hiii")
        Firstname= request.POST.get('Firstname')
        Lastname= request.POST.get('Lastname')
        Dateofbirth=request.POST.get('Dateofbirth')
        print(Firstname)
        Gender=request.POST.get('Gender')
        print(Gender)
        print("######")
        Maritial=request.POST.get('Maritial')
        print(Maritial)
        Nationality=request.POST.get('Nationality')
        Email = request.POST.get('Email')
        Address=request.POST.get('Address')
        City=request.POST.get('City')
        State=request.POST.get('State')
        Country=request.POST.get('Country')
        Phonenumber= request.POST.get('Phonenumber')
        print(Email)
        print(request.session['Email1'])
        print("done")
        if(Email!=request.session['Email1']):
            print("hii")
            error_message="ohh your email doesn't matched with login mail"
            return render(request,'student_portal/Personal_details.html',{'error':error_message})
        else:
            student=Student.get_student_by_email(Email)
            stdind1=Stdind.get_stdind_by_email(student.Email)
            #if(City==None or Country == None):
             #   City=Stdind1.City
             #   Country=Stdind1.Country
            stdind=Stdind(Firstname= Firstname,Lastname= Lastname,Dateofbirth=Dateofbirth,Gender=Gender,
            Maritial=Maritial,Nationality=Nationality,Email = Email,Address=Address,City=City,State=State,
            Country=Country,Phonenumber= Phonenumber)
            if(stdind1):
                stdind1.delete()
            stdind.register()
            value={'Firstname': Firstname,'Lastname': Lastname,'Dateofbirth':Dateofbirth,'Gender':Gender,
            'Maritial':Maritial,'Nationality':Nationality,'Email' : Email,'Address':Address,'City':City,'State':State,
            'Country':Country,'Phonenumber': Phonenumber}
            data={'value':value}
            return render(request,'student_portal/Personal_details.html',data)

class stdacd(View):
    def get(self,request):
        data={}
        student=Student.get_student_by_email(request.session['Email1'])
        if(student):
            stdacd=Stdacd.get_stdacd_by_email(student.Email)
        if(stdacd):
            value={'Sscqual':stdacd.Sscqual,'Sscname':stdacd.Sscname,'Sscdate':stdacd.Sscdate,'Sscmarks':stdacd.Sscmarks,'Sscgrading':stdacd.Sscgrading,'SscDoc':stdacd.SscDoc,
                'Intqual':stdacd.Intqual,'Intname':stdacd.Intname,'Intdate':stdacd.Intdate,'Intmarks':stdacd.Intmarks,'Intgrading':stdacd.Intgrading,
                'IntDoc':stdacd.IntDoc,'Uniqual':stdacd.Uniqual,'Uniname':stdacd.Uniname,'Unicname':stdacd.Unicname,'Unidate':stdacd.Unidate,'Unimarks': stdacd.Unimarks,
                'Unigrading':stdacd.Unigrading,'UniDoc':stdacd.UniDoc}
            data={'value':value}
        return render(request,'student_portal/Academic _Details.html',data)
    def post(self,request):
        print("in post man in stddetail")
        Email=request.session['Email1']
        Sscqual=request.POST.get('Sscqual')
        print("123456")
        print(Sscqual)
        Sscname=request.POST.get('Sscname')
        Sscdate=request.POST.get('Sscdate')
        Sscmarks=request.POST.get('Sscmarks')
        Sscgrading=request.POST.get('Sscgrading')
        SscDoc=request.FILES['SscDoc']

        fs=FileSystemStorage()
        name=fs.save(SscDoc.name,SscDoc)
        url=fs.url(name)
        print(url)
        Intqual=request.POST.get('Intqual')
        Intname=request.POST.get('Intname')
        Intdate=request.POST.get('Intdate')
        Intmarks=request.POST.get('Intmarks')
        Intgrading=request.POST.get('Intgrading')
        IntDoc=request.FILES['IntDoc']

        name1=fs.save(IntDoc.name,IntDoc)
        url1=fs.url(name1)
        Uniqual=request.POST.get('Uniqual')
        Uniname=request.POST.get('Uniname')
        Unicname=request.POST.get('Unicname')
        Unidate=request.POST.get('Unidate')
        Unimarks=request.POST.get('Unimarks')
        Unigrading=request.POST.get('Unigrading')
        UniDoc=request.FILES['UniDoc']

        name2=fs.save(UniDoc.name,UniDoc)
        url2=fs.url(name2)
        stdacd=Stdacd(Email=Email,Sscqual=Sscqual,Sscname=Sscname,Sscdate=Sscdate,Sscmarks=Sscmarks,Sscgrading=Sscgrading,SscDoc=SscDoc,
            Intqual=Intqual,Intname=Intname,
            Intdate=Intdate,
            Intmarks=Intmarks,Intgrading=Intgrading,IntDoc=IntDoc,Uniqual=Uniqual,Uniname=Uniname,Unicname=Unicname
            ,Unidate=Unidate,Unimarks=Unimarks,Unigrading=Unigrading,UniDoc=UniDoc)

        student=Student.get_student_by_email(Email)
        stdacd1=Stdacd.get_stdacd_by_email(student.Email)
        if(stdacd1):
            stdacd1.delete()
        stdacd.register()
        value={'Sscqual':Sscqual,'Sscname':Sscname,'Sscdate':Sscdate,'Sscmarks':Sscmarks,'Sscgrading':Sscgrading,'SscDoc':url,
            'Intqual':Intqual,'Intname':Intname,'Intdate':Intdate,'Intmarks':Intmarks,'Intgrading':Intgrading,
            'IntDoc':url1,'Uniqual':Uniqual,'Uniname':Uniname,'Unicname':Unicname,'Unidate':Unidate,'Unimarks': Unimarks,
            'Unigrading':Unigrading,'UniDoc':url2}
        data={'value':value}
        return render(request,'student_portal/Academic _Details.html',data)
class stdcour(View):
    def get(self,request):
        data={}
        student=Student.get_student_by_email(request.session['Email1'])
        if(student):
            stdcour=Stdcour.get_stdcour_by_email(student.Email)
        if(stdcour):
            value={'Applyingfor':stdcour.Applyingfor,'Date':stdcour.Date,'pcoun1':stdcour.pcoun1,'pcoun2':stdcour.pcoun2,'pcoun3':stdcour.pcoun3,'pcour4':stdcour.pcour4,'pcour5':stdcour.pcour5,'pcour6':stdcour.pcour6}
            data={'value':value}
        return render(request,'student_portal/Course_application.html',data)
    def post(self,request):
        Email=request.session['Email1']
        Applyingfor=request.POST.get('Applyingfor')
        Date=request.POST.get('Date')
        pcoun1=request.POST.get('pcoun1')
        pcoun2=request.POST.get('pcoun2')
        pcoun3=request.POST.get('pcoun3')
        pcour4=request.POST.get('pcour4')
        pcour5=request.POST.get('pcour5')
        pcour6=request.POST.get('pcour6')

        print(pcoun1)

        stdcour=Stdcour(Applyingfor=Applyingfor,Date=Date,pcoun1=pcoun1,pcoun2=pcoun2,
        pcoun3=pcoun3,pcour4=pcour4,pcour5=pcour5,pcour6=pcour6,Email=Email)
        student=Student.get_student_by_email(Email)
        stdcour1=Stdcour.get_stdcour_by_email(student.Email)
        if(stdcour1):
            stdcour1.delete()
        stdcour.register()
        value={'Applyingfor':Applyingfor,'Date':Date,'pcoun1':pcoun1,'pcoun2':pcoun2,'pcoun3':pcoun3,'pcour4':pcour4,'pcour5':pcour5,'pcour6':pcour6}
        data={'value':value}
        return render(request,'student_portal/Course_application.html',data)
class stdpro(View):
    def get(self,request):
        data={}
        student=Student.get_student_by_email(request.session['Email1'])
        if(student):
            stdpro=Stdpro.get_stdpro_by_email(student.Email)
            stdpro1=Stdpro1.get_stdpro1_by_email(student.Email)
        if(stdpro):
            testeng=[]
            yeareng=[]
            overallscoreeng=[]
            uploadeng=[]
            for i in range(0,len(stdpro)):
                testeng.append(stdpro[i].Testeng)
                yeareng.append(stdpro[i].Yeareng)
                overallscoreeng.append(stdpro[i].Overallscoreeng)
                uploadeng.append(stdpro[i].Urleng)
            list=[]
            for i in range(0,len(stdpro)):
                list.append({'Testeng':testeng[i],
                         'Yeareng':yeareng[i],
                              'Overallscoreeng':overallscoreeng[i],
                                                  'Uploadeng':uploadeng[i]})
            
            data['stdpro']=list
            print(list)
        if(stdpro1):
            testad=[]
            yearad=[]
            overallscoread=[]
            uploadad=[]
            for i in range(0,len(stdpro1)):
                testad.append(stdpro1[i].Testad)
                yearad.append(stdpro1[i].Yearad)
                overallscoread.append(stdpro1[i].Overallscoread)
                uploadad.append(stdpro1[i].Urlad)
            list1=[]
            for i in range(0,len(stdpro1)):
                list1.append({'Testad':testad[i],
                         'Yearad':yearad[i],
                              'Overallscoread':overallscoread[i],
                                                  'Uploadad':uploadad[i]})
            data['stdpro1']=list1
            print(list1)
            print(data)
            
        return render(request,'student_portal/professional_qualification.html',data)
    def post(self,request):
        Email=request.session['Email1']
        Testeng=request.POST.getlist('Testeng[]')
        Yeareng=request.POST.getlist('Yeareng[]')
        Overallscoreeng=request.POST.getlist('Overallscoreeng[]')

        Testad=request.POST.getlist('Testad[]')
        Yearad=request.POST.getlist('Yearad[]')
        Overallscoread=request.POST.getlist('Overallscoread[]')
        fs=FileSystemStorage()
        Uploadeng=request.FILES.getlist('Uploadeng[]')
        print("webfWJEFBJEfliwejhfiWNFLIH")
        print(Testeng)
        print(Yeareng)
        print(Overallscoreeng)
        print(Uploadeng)
        print(Testad)
        print(Yearad)
        print(Overallscoread)
        Uploadad=request.FILES.getlist('Uploadad[]')
        print(Uploadad)
        urleng=[]
        urlad=[]
        for i in range(0,len(Testeng)):
            testeng=Testeng[i]
            yeareng=Yeareng[i]
            overallscoreeng=Overallscoreeng[i]
            uploadeng=Uploadeng[i]
            name=fs.save(uploadeng.name,uploadeng)
            url=fs.url(name)
            urleng.append(url)
            stdpro=Stdpro(Email=Email,Testeng=testeng,Yeareng=yeareng,Overallscoreeng=overallscoreeng,Uploadeng=uploadeng,Urleng=url)
            stdpro.register()

        for i in range(0,len(Testad)):
            testad=Testad[i]
            yearad=Yearad[i]
            overallscoread=Overallscoread[i]
            uploadad=Uploadad[i]
            name=fs.save(uploadad.name,uploadad)
            url=fs.url(name)
            urlad.append(url)
            stdpro1=Stdpro1(Email=Email,Testad=testad,Yearad=yearad,Overallscoread=overallscoread,Uploadad=uploadad,Urlad=url)
            stdpro1.register()


        '''name3=fs.save(Uploadeng.name,Uploadeng)
        url3=fs.url(name3)

        
        name5=fs.save(Uploadad.name,Uploadad)
        url5=fs.url(name5)
        
        print(url3)'''
        '''stdpro=Stdpro(Email=Email,Testeng=Testeng,Yeareng=Yeareng,Overallscoreeng=Overallscoreeng,Uploadeng=Uploadeng,
            Testad=Testad,Yearad=Yearad,Overallscoread=Overallscoread,Uploadad=Uploadad)
        stdpro.register()'''
        value={'Testeng': Testeng,'Yeareng':Yeareng,'Overallscoreeng': Overallscoreeng,'Uploadeng':urleng,
            'Testad': Testad,'Yearad': Yearad,'Overallscoread':Overallscoread,'Uploadad':urlad}
        data={'value':value}
        return redirect("stdpro")

class stdhome(View):
    def get(self,request):
       
        #print(request.user.first_name)
        #print(request.user.username)
        #print(request.user.email)
        #print(request.user.phonenumber)
        try:
            #print(request.session['Email1'])
            
            student=Student.objects.get(Email=request.session['Email1'])
            
        except:
             Firstname= request.user.first_name
             Phonenumber=None
             Email = request.user.email
             Password = None
             Confirmpassword = None

             
             student=Student(Firstname=Firstname,Phonenumber=Phonenumber,Email=Email,Password=Password,Confirmpassword=Confirmpassword)
             if(Student.objects.get(Email=Email)==None):
                 student.register()

             request.session['Email1']=Email
             request.session['Firstname1']=Firstname
             print(request.session['Email1'])

             users=User.objects.all().filter(email=request.session['Email1'])
    
             if(users):
                 for user in range(1,len(users)):
                     users[user].delete()

             student=Student.objects.get(Email=Email)
    

        

        value={'Name':student.Firstname}
        data={}
        data['value']=value

        return render(request,'student_portal/index.html',data)
class stdsaved(View):
    def get(self,request,name="a"):
        if(name=="a"):
            saved_univ=Saved.objects.filter(Mail=request.session['Email1'])
            print('rohit')
            print(saved_univ)
            data={}
            for i in saved_univ:
                print(i.Universityname)
            #print(saved_univ.Univerisityname)
            data['saved_univ']=saved_univ
            return render(request,'student_portal/saved.html',data)
        else:
            university=Saved.objects.filter(Mail=request.session['Email1']).filter(Universityname=name)
            university.delete()
            return redirect('saved')


    def post(self,request,name="a"):
        print('###')
        university=University.objects.get(Firstname=name)
        univdetail=Univdetail.objects.get(Email=university.Email)
        unicon=Univcon.objects.get(Email=university.Email)
        name=university.Firstname
        Phonenumber=university.Phonenumber
        About=univdetail.About
        Mail=request.session['Email1']
        Location=unicon.Location
        print(request.session['Email1'])
        flag=Saved.objects.filter(Mail=Mail)
        print(flag)
        print(name)
        print("##")
        count=0
        for i in flag:
            count=0
            print(i.Universityname)
            if i.Universityname == name:
                count=1
            if count == 1:
                break
        if count == 0:
            saved=Saved(Universityname=name,About=About,Mail=Mail,Phonenumber=Phonenumber,Location=Location)
            saved.register()
            return redirect('search')
        return redirect('search')
class stdsecurity(View):
    def get(self,request):
        student1=Student.get_student_by_email(request.session['Email1'])
        print(student1.Phonenumber)
        data={'Phonenumber':student1.Phonenumber}
        return render(request,'student_portal/Password_security.html',data)
    def post(self,request):
        data={}
        student1=Student.get_student_by_email(request.session['Email1'])
        Phonenumber=request.POST.get('Phonenumber')
        if(Phonenumber!=None):
            student1.Phonenumber=Phonenumber
            print(student1.Phonenumber)
            student1.register()
        a=student1.Password
        Password=request.POST.get('Password')
        Confirmpassword=request.POST.get('Confirmpassword')
        Confirmpassword1=request.POST.get('Confirmpassword1')
        error_message=None
        flag=check_password(Password,a)
        if(Phonenumber):
            data={'Phonenumber':student1.Phonenumber}
            return render(request,'student_portal/Password_security.html',data)
        if(flag):
            if(Confirmpassword == Confirmpassword1):

                student1.Password=make_password(Confirmpassword)
                student1.Confirmpassword=make_password(Confirmpassword1)
                student1.register()
                data={'Phonenumber':student1.Phonenumber}
                return render(request,'student_portal/Password_security.html',data)
            else:
                
                error_message='Password and current password doesnt match !!!'
                data={'Phonenumber':student1.Phonenumber}
                data['error']=error_message

                return render(request,'student_portal/Password_security.html',data)
        else:
            error_message='Current Password is invalid!!!'
            data={'Phonenumber':student1.Phonenumber}
            data['error']=error_message
            return render(request,'student_portal/Password_security.html',data)

class stdappli(View):
    def get(self,request,name="a",name1="b",name2="c"):
        try:
            student=Student.objects.get(Firstname=name)
        except:
            student=False
        university=University.objects.get(Firstname=name1)
        if(student):
            stdcour=Stdcour.objects.get(Email=student.Email)
            stdname=student.Firstname
            stdmail=student.Email
        else:
            student=Stdind.objects.get(Firstname=name)
            stdcour=Stdcour.objects.get(Email=student.Email)
            stdname=student.Firstname
            stdmail=student.Email
        univname=university.Firstname
        
        univmail=university.Email
        date=datetime.date(datetime.now())
        program=stdcour.Applyingfor
        std=Stdappli.objects.filter(stdmail=stdmail)
        status='applied'
        if(name2=='c'):
            name2='-'
        savedappli=Stdappli(stdname=stdname,univname=univname,stdmail=stdmail,univmail=univmail,
        date=date,program=program,status=status,agentmail=name2)
        try:
            saved=Stdappli.objects.filter(univmail=univmail).get(stdmail=stdmail)
            if(saved):
                saved.delete()
        except:
            pass
        savedappli.register()
        #return redirect('/overview/'+univname+'/')
        return redirect('agent_home')
    def post(self,request,name="a",name1="b",name2="c"):
        student=Student.objects.get(Firstname=name)
        university=University.objects.get(Firstname=name1)
        if(student):
            stdcour=Stdcour.objects.get(Email=student.Email)
            stdname=student.Firstname
            stdmail=student.Email
        else:
            student=stdind.objects.get(Firstname=name)
            stdcour=Stdcour.objects.get(Email=stdind.Email)
            stdname=student.Firstname
            stdmail=student.Email
        univname=university.Firstname
        
        univmail=university.Email
        date=datetime.date(datetime.now())
        program=stdcour.Applyingfor
        std=Stdappli.objects.filter(stdmail=stdmail)
        status='applied'
        if(name2=='c'):
            name2='-'
        
        savedappli=Stdappli(stdname=stdname,univname=univname,stdmail=stdmail,univmail=univmail,
        date=date,program=program,status=status,agentmail=name2)
        try:
            saved=Stdappli.objects.filter(univmail=univmail).get(stdmail=stdmail)
            if(saved):
                saved.delete()
        except:
            pass
        savedappli.register()
        #return redirect('/overview/'+univname+'/')
        return redirect('/student/applied')
class stdapplicour(View):
    def get(self,request,name="a",name1="b",name2="c"):
        value={'name':name,'name1':name1,'name2':name2}
        university=University.objects.get(Firstname=name1)
        print(university)
        Email=university.Email
        cour=Courses.objects.filter(Email=Email)

        application1=Application.objects.get(Email=Email)
        fee=application1.Applyfee
        value['cour']=cour
        value['fee']=fee

        return render(request,'student_portal/course.html',{'value':value})
    def post(self,request,name="a",name1="b",name2="c"):
        print("gruy")
        count=Stdappli.objects.all().count()
        id=count+1
        fee=request.POST.get('fee')
        coursename=request.POST.get('Name')
        print(coursename)
        name=name
        name1=name1
        student=Student.objects.get(Firstname=name)
        university=University.objects.get(Firstname=name1)
        if(student):
            stdcour=Stdcour.objects.get(Email=student.Email)
            stdname=student.Firstname
            stdmail=student.Email
        else:
            student=stdind.objects.get(Firstname=name)
            stdcour=Stdcour.objects.get(Email=stdind.Email)
            stdname=student.Firstname
            stdmail=student.Email
        univname=university.Firstname
        
        univmail=university.Email
        date=datetime.date(datetime.now())
        program=stdcour.Applyingfor
        std=Stdappli.objects.filter(stdmail=stdmail)
        status='applied'
        if(name2=='c'):
            name2='-'
        
        savedappli=Stdappli(pstatus="process",id=id,stdname=stdname,univname=univname,stdmail=stdmail,univmail=univmail,
        date=date,program=program,status=status,agentmail=name2,Coursename=coursename,fee=fee)
        try:
            saved=Stdappli.objects.filter(univmail=univmail).get(stdmail=stdmail)
            if(saved):
                saved.delete()
        except:
            pass
        savedappli.register()
        value={'name':name,'name1':name1,'name2':name2}
        university=University.objects.get(Firstname=name1)
        print(university)
        Email=university.Email
        cour=Courses.objects.filter(Email=Email)

        application1=Application.objects.get(Email=Email)
        fee=application1.Applyfee
        value['cour']=cour
        value={'id':id,'stdname':stdname,'univname':univname,'stdmail':stdmail,'univmail':univmail,
        'date':date,'program':program,'status':status,'agentmail':name2,'Coursename':coursename,'fee':fee}
        
        #return redirect('/student/applied')
        return render(request,'student_portal/course.html',{'value':value})


    







