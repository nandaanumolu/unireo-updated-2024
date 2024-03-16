from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from portal.models.eventsinfo import Event,Blog
from django.core.files.storage import FileSystemStorage
from portal.models.universityinfo import University
from portal.models.univdetail import Univdetail
from portal.models.courses import Courses
from portal.models.stdappli import Stdappli
from django.core.files.storage import FileSystemStorage
from portal.models.offer import Offerletter
def landing(request):
    return render(request,'signup/Landing_page.html')
class stu_accept(View):
    def get(self,request,name="a"):
        data={}
        data['name']=name
        return render(request,'bio1.html',data)
    def post(self,request):
        print("nanda")
        Name=request.POST.get('Name')
        Letter=request.FILES['Letter']
        fs=FileSystemStorage()
        name=fs.save(Letter.name,Letter)
        url=fs.url(name)
        Email=request.session['Email']
        offer=Offerletter(Letter=Letter,Name=Name,Email=Email)
        offer.register()

        stddetail=Stdappli.objects.filter(stdname=Name).get(univmail=request.session['Email'])
        print(Name)
        print(stddetail)
        
        stddetail.status="accept"
        stddetail.register()
        return redirect('/applicants')

def stu_reject(request,name="a"):
    print("anumolu")
    stddetail=Stdappli.objects.filter(stdname=name).get(univmail=request.session['Email'])
    stddetail.status="reject"
    stddetail.register()
    return redirect('/applicants')


def home(request):
    stddetail=Stdappli.objects.filter(univmail=request.session['Email'])
    count=Stdappli.objects.filter(univmail=request.session['Email']).count()
    accept=Stdappli.objects.filter(univmail=request.session['Email']).filter(status="accept").count()
    reject=Stdappli.objects.filter(univmail=request.session['Email']).filter(status="reject").count()
    applied=Stdappli.objects.filter(univmail=request.session['Email']).filter(status="applied").count()
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
    return render(request,'home_content.html',data)
def table(request):
    stddetail=Stdappli.objects.filter(univmail=request.session['Email']).filter(pstatus="succeeded")
    data={}
    data['stddetail']=stddetail
    return render(request,'All_Applications.html',data)
class overview(View):
    def get(self,request,name="a"):
        if(name=="a"):
            return render(request,'Overview.html')
        else:
            university=University.objects.get(Firstname=name)
            unidetail=Univdetail.objects.get(Email=university.Email)
            cour_list=Courses.objects.filter(Email=university.Email)
            eve_list=Event.objects.filter(Email=university.Email)
            blo_list=Blog.objects.filter(Email=university.Email)
            data={}
            data={'university':university,'unidetail':unidetail,
            'cour_list':cour_list,
            'eve_list':eve_list,
            'blo_list':blo_list}
            
            #return render(request,'Overview.html',data)
            return render(request,'test_overview.html',data)

def support(request):
    return render(request,'support.html')

class events(View):
    def get(self,request,name="a",name1="b"):
        if(name=="a"):
            savedevents=Event.objects.filter(Email=request.session['Email'])
            data={'listeve':savedevents}
            return render(request,'Events.html',data)
        elif(name1=="delete"):
            savedevents=Event.objects.filter(Email=request.session['Email']).filter(Ename=name)
            savedevents.delete()
            return redirect('events')
        elif(name1=="edit"):
            data={}
            print(request.session['Email'])
            university= University.get_university_by_email(request.session['Email'])
            print(university.Email)
            qwe="rty"
            print(qwe)
            if(university):
                savedevents=Event.objects.all().filter(Email=university.Email).get(Ename=name)
                value={'Ename':savedevents.Ename,  'Edate':savedevents.Edate, 'Edetails':savedevents.Ephoto,
                'Ephoto':savedevents.Ephoto,'Email':savedevents.Email}
            data={'value':value}
            return render(request,'AddEvents.html',data)


class addblog(View):
    def get(self,request):
        return render(request,'AddBlog.html')
    def post(self,request):
        bname=request.POST.get('Bname')
        bdate=request.POST.get('Bdate')
        bdetail=request.POST.get('Bdetail')
        bdoc=request.FILES['Bphoto']
        fs=FileSystemStorage()
        name=fs.save(bdoc.name,bdoc)
        url=fs.url(name)
        print(url)

        Email=request.session['Email']
        blog=Blog(Bname=bname,Bdate=bdate,Bdetail=bdetail,Bphoto=url,Email=Email)
        try:
            checkingforexistance=Blog.objects.filter(Email=Email).get(Bname=bname)
            if(checkingforexistance):
                checkingforexistance.delete()
        except:
            pass
        blog.register()
        return redirect("allblog")
class allblog(View):
    def get(self,request,name="a",name1="b"):
        if(name=="a"):
            savedblogs=Blog.objects.filter(Email=request.session['Email'])
            data={'listblo':savedblogs}
            return render(request,'AllBlogs.html',data)
        elif(name1=="delete"):
            savedblogs=Blog.objects.filter(Email=request.session['Email']).filter(Bname=name)
            savedblogs.delete()
            return redirect('allblog')
        elif(name1=="edit"):
            data={}
            print(request.session['Email'])
            university= University.get_university_by_email(request.session['Email'])
            print(university.Email)
            if(university):
                savedblogs=Blog.objects.all().filter(Email=university.Email).get(Bname=name)
                value={'Bname':savedblogs.Bname,  'Bdate':savedblogs.Bdate, 'Bdetails':savedblogs.Bphoto,
                'Bphoto':savedblogs.Bphoto,'Email':savedblogs.Email}
                data={'value':value}
                return render(request,'AddBlog.html',data)
def applicationform(request):
    return render(request,'ApplicationForm.html')
def student(request):
    return render(request,'student_portal/student_nav.html')
def blogs(request):
    return render(request,'All_Blogs.html')
def security(request):
    return render(request,'Security.html')

def newapplication(request):
    stddetail=Stdappli.objects.filter(univmail=request.session['Email']).filter(status="accept").filter(pstatus="succeeded")
    data={}
    data['stddetail']=stddetail
    return render(request,'NewApplications.html',data)
def inprogressapplication(request):
    stddetail=Stdappli.objects.filter(univmail=request.session['Email']).filter(status="applied").filter(pstatus="succeeded")
    data={}
    data['stddetail']=stddetail
    return render(request,'InProgressApplication.html',data)
def rejectedapplication(request):
    stddetail=Stdappli.objects.filter(univmail=request.session['Email']).filter(status="reject").filter(pstatus="succeeded")
    data={}
    data['stddetail']=stddetail
    return render(request,'RejectedApplication.html',data)
