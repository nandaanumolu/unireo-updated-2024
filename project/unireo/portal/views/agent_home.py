from django.shortcuts import render
from portal.models.stdappli import Stdappli
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from portal.models.consultancyinfo import Consultancy
from portal.models.universityinfo import University
from portal.models.stddetail import Stdacd,Stdpro,Stdind,Stdcour,Stdpro1
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from django.core.files.storage import FileSystemStorage
from portal.models.studentinfo import Student
from portal.models.consultdetails import Consultancydetails
from portal.models.courses import Courses

def agent_home(request):
    stddetail=Stdappli.objects.filter(agentmail=request.session['Email2'])
    count=Stdappli.objects.filter(agentmail=request.session['Email2']).count()
    accept=Stdappli.objects.filter(agentmail=request.session['Email2']).filter(status="accept").count()
    reject=Stdappli.objects.filter(agentmail=request.session['Email2']).filter(status="reject").count()
    applied=Stdappli.objects.filter(agentmail=request.session['Email2']).filter(status="applied").count()
    try:
        accper=(accept/count)*100
        rejper=(reject/count)*100
        appper=(applied/count)*100
        couper=(count/count)*100
    except:
        
        accper=0
        rejper=0
        appper=0
        couper=0
    if(len(stddetail)>6):
        stddetail=stddetail[0:6]
    data={}
    data['stddetail']=stddetail
    data['accept']=accept
    data['applied']=applied
    data['reject']=reject
    data['count']=count
    data['stddetail']=stddetail
    data['accper']=accper
    data['appper']=appper
    data['rejper']=rejper
    data['couper']=couper
    return render(request,'agent_portal/index.html',data)
def table(request):
    stddetail=Stdappli.objects.filter(univmail=request.session['Email'])
    data={}
    data['stddetail']=stddetail
    return render(request,'agent_portal/index.html')
def agent_application(request):
    applications=Stdappli.objects.filter(agentmail=request.session['Email2'])
    value={}
    value['applications']=applications
    data={}
    data['value']=value
    return render(request,'agent_portal/all_applications.html',data)
def agent_inprogress_application(request):
    applications=Stdappli.objects.filter(agentmail=request.session['Email2']).filter(status="applied")
    print(applications)
    value={}
    value['applications']=applications
    data={}
    data['value']=value
    return render(request,'agent_portal/inprogress_applications.html',data)
def agent_rejected_application(request):
    applications=Stdappli.objects.filter(agentmail=request.session['Email2']).filter(status="reject")
    value={}
    value['applications']=applications
    data={}
    data['value']=value
    return render(request,'agent_portal/rejected_applications.html',data)
def agent_new_application(request):
    applications=Stdappli.objects.filter(agentmail=request.session['Email2']).filter(status="accept")
    value={}
    value['applications']=applications
    data={}
    data['value']=value
    return render(request,'agent_portal/new_applications.html',data)

def agent_support(request):
    return render(request,'agent_portal/support.html')
def new_applicant(request):
    applications=Stdappli.objects.filter(agentmail=request.session['Email2']).filter(status="accept")
    value={}
    value['applications']=applications
    data={}
    data['value']=value
    return render(request,'agent_portal/new_applicant_form.html',data)
    
class agent_academic(View):
    def get(self,request):
        return render(request,'agent_portal/academic.html')
    def post(self,request):
        print("in post man in stddetail")
        Email=request.session['agn_stdmail']
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
        agentid=request.session['agentid']
        agentmail=request.session['Email2']

        name2=fs.save(UniDoc.name,UniDoc)
        url2=fs.url(name2)
        stdacd=Stdacd(Email=Email,Sscqual=Sscqual,Sscname=Sscname,Sscdate=Sscdate,Sscmarks=Sscmarks,Sscgrading=Sscgrading,SscDoc=SscDoc,
            Intqual=Intqual,Intname=Intname,
            Intdate=Intdate,
            Intmarks=Intmarks,Intgrading=Intgrading,IntDoc=IntDoc,Uniqual=Uniqual,Uniname=Uniname,Unicname=Unicname
            ,Unidate=Unidate,Unimarks=Unimarks,Unigrading=Unigrading,UniDoc=UniDoc,Agentid=agentid,Agentmail=agentmail)

        stdacd.register()
        value={'Sscqual':Sscqual,'Sscname':Sscname,'Sscdate':Sscdate,'Sscmarks':Sscmarks,'Sscgrading':Sscgrading,'SscDoc':url,
            'Intqual':Intqual,'Intname':Intname,'Intdate':Intdate,'Intmarks':Intmarks,'Intgrading':Intgrading,
            'IntDoc':url1,'Uniqual':Uniqual,'Uniname':Uniname,'Unicname':Unicname,'Unidate':Unidate,'Unimarks': Unimarks,
            'Unigrading':Unigrading,'UniDoc':url2}
        data={'value':value}
        return render(request,'agent_portal/academic.html',data)
    
class agent_course(View):
    def get(self,request):
        universities=University.objects.all()
        data={}
        data["universities"]=universities
        
        return render(request,'agent_portal/Course.html',data)
    def post(self,request):
        Email=request.session['agn_stdmail']

        Applyingfor=request.POST.get('Applyingfor')
        Date=request.POST.get('Date')
        pcoun1=request.POST.get('pcoun1')
        pcoun2=request.POST.get('pcoun2')
        pcoun3=request.POST.get('pcoun3')
        pcour4=request.POST.get('pcour4')
        pcour5=request.POST.get('pcour5')
        pcour6=request.POST.get('pcour6')
        agentid=request.session['agentid']
        agentmail=request.session['Email2']
        univ_name=request.POST.get("univname")

        stdind=Stdind.get_stdind_by_email(Email)
        name=stdind.Firstname

        print(pcoun1)

        stdcour=Stdcour(Agentid=agentid,Agentmail=agentmail,Applyingfor=Applyingfor,Date=Date,pcoun1=pcoun1,pcoun2=pcoun2,
        pcoun3=pcoun3,pcour4=pcour4,pcour5=pcour5,pcour6=pcour6,Email=Email,Univname=univ_name)
        stdcour.register()
        value={'Applyingfor':Applyingfor,'name':name,'univname':univ_name,'agentmail':agentmail,'Date':Date,'pcoun1':pcoun1,'pcoun2':pcoun2,'pcoun3':pcoun3,'pcour4':pcour4,'pcour5':pcour5,'pcour6':pcour6}
        data={'value':value}
        return render(request,'agent_portal/Course.html',data)
class agent_personal(View):
    print("qazxsw")
    def get(self,request):
        return render(request,'agent_portal/Personal.html')
    def post(self,request):
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
        request.session['agn_stdmail']=Email
        Address=request.POST.get('Address')
        City=request.POST.get('City')
        State=request.POST.get('State')
        Country=request.POST.get('Country')
        Phonenumber= request.POST.get('Phonenumber')
        print(request.session['Email2'])
        agentid=request.session['agentid']
        agentmail=request.session['Email2']
        print("done")
        student=Student(Firstname=Firstname,
        Phonenumber=Phonenumber,Email =Email ,Password = None,Confirmpassword =None )
        student.register()
        stdind=Stdind(Firstname= Firstname,Lastname= Lastname,Dateofbirth=Dateofbirth,Gender=Gender,
            Maritial=Maritial,Nationality=Nationality,Email = Email,Address=Address,City=City,State=State,
            Country=Country,Phonenumber= Phonenumber,Agentid=agentid,Agentmail=agentmail)
        stdind.register()
        value={'Firstname': Firstname,'Lastname': Lastname,'Dateofbirth':Dateofbirth,'Gender':Gender,
                'Maritial':Maritial,'Nationality':Nationality,'Email' : Email,'Address':Address,'City':City,'State':State,
                'Country':Country,'Phonenumber': Phonenumber}
        data={'value':value}
        return render(request,'agent_portal/Personal.html',data)
    
    
class agent_professional(View):
    def get(self,request):    
        return render(request,'agent_portal/Profressional.html')
    def post(self,request):
        Email=request.session['agn_stdmail']
        Testeng=request.POST.getlist('Testeng[]')
        Yeareng=request.POST.getlist('Yeareng[]')
        Overallscoreeng=request.POST.getlist('Overallscoreeng[]')
        agentid=request.session['agentid']
        agentmail=request.session['Email2']

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
            stdpro=Stdpro(Agentmail=agentmail,Agentid=agentid,Email=Email,Testeng=testeng,Yeareng=yeareng,Overallscoreeng=overallscoreeng,Uploadeng=uploadeng,Urleng=url)
            stdpro.register()

        for i in range(0,len(Testad)):
            testad=Testad[i]
            yearad=Yearad[i]
            overallscoread=Overallscoread[i]
            uploadad=Uploadad[i]
            name=fs.save(uploadad.name,uploadad)
            url=fs.url(name)
            urlad.append(url)
            stdpro1=Stdpro1(Agentmail=agentmail,Agentid=agentid,Email=Email,Testad=testad,Yearad=yearad,Overallscoread=overallscoread,Uploadad=uploadad,Urlad=url)
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
        return render(request,'agent_portal/Profressional.html')
def agent_overview(request):
    return render(request,'agent_portal/agent_overview.html')
def agent_update(request):
    return render(request,'agent_portal/agent_update.html')

class agent_security(View):
    def get(self,request):
        agent1=Consultancy.get_consultancy_by_email(request.session['Email2'])
        print(agent1.Phonenumber)
        data={'Phonenumber':agent1.Phonenumber}
        return render(request,'agent_portal/security.html',data)
    def post(self,request):
        data={}
        agent1=Consultancy.get_consultancy_by_email(request.session['Email2'])
        Phonenumber=request.POST.get('Phonenumber')
        Phonenumber=agent1.Phonenumber
        #print(student1.Phonenumber)
        agent1.register()
        a=agent1.Password
        Password=request.POST.get('Password')
        Confirmpassword=request.POST.get('Confirmpassword')
        Confirmpassword1=request.POST.get('Confirmpassword1')
        error_message=None
        flag=check_password(Password,a)
        if(Phonenumber):
            data={'Phonenumber':agent1.Phonenumber}
            return render(request,'agent_portal/security.html',data)
        if(flag):
            if(Confirmpassword == Confirmpassword1):

                agent1.Password=make_password(Confirmpassword)
                agent1.Confirmpassword=make_password(Confirmpassword1)
                agent1.register()
                return render(request,'agent_portal/security.html',data)
            else:
                
                error_message='Password and current password doesnt match !!!'
                data['error']=error_message

                return render(request,'agent_portal/security.html',data)
        else:
            error_message='Current Password is invalid!!!'
            data['error']=error_message
            return render(request,'agent_portal/security.html',data)

class Consultbank(View):
    def get(self,request):
        value={}
        try:
            cons=Consultancydetails.objects.get(Email=request.session['Email2'])
            print(cons)
            value={'Cname': cons.Cname, 'Aid':cons.Aid,'Aadd':cons.Aadd,'Email':cons.Email,
                'Bname':cons.Bname,'Accountnumber':cons.Accountnumber,'Branch':cons.Branch,'Ifsccode':cons.Ifsccode}
        except:
            pass
        return render(request,'agent_portal/basic.html',{'value':value})
    def post(self,request):
        Cname= request.POST.get('Cname')
        Aid=request.session['agentid']
        Aadd=request.POST.get('Aadd')
        Email=request.session['Email2']
        Bname=request.POST.get('Bname')
        Accountnumber=request.POST.get('Accountnumber')
        Branch=request.POST.get('Branch')
        Ifsccode=request.POST.get('Ifsccode')

        cons1=Consultancydetails.objects.all().filter(Email=request.session['Email2'])
    
        cons=Consultancydetails(Cname= Cname, Aid=Aid,Aadd=Aadd,Email=Email,
              Bname=Bname,Accountnumber=Accountnumber,Branch=Branch,Ifsccode=Ifsccode   )
        if(cons1):
            cons1.delete()
        cons.register()

        value={'Cname': Cname, 'Aid':Aid,'Aadd':Aadd,'Email':Email,
              'Bname':Bname,'Accountnumber':Accountnumber,'Branch':Branch,'Ifsccode':Ifsccode}

        return render(request,'agent_portal/basic.html',{'value':value})

class viewcommision(View):
    def get(self,request,name="a"):
        university=University.objects.all()
        data={}
        data['university']=university       
        return render(request,'agent_portal/viewcommision.html',data)

    def post(self,request):
        name=request.POST.get('uniname')
        university=University.objects.all()
        unimail=University.objects.get(Firstname=name).Email
        courses1=Courses.objects.filter(Email=unimail)
        print(courses1)
        data={}
        data['courses1']=courses1
        data['university']=university
        data['uniname']=name
        return render(request,'agent_portal/viewcommision.html',data)

