from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from portal.models.universityinfo import University
from portal.models.univdetail import Univdetail,Univcon
from portal.models.stddetail import Stdacd,Stdpro,Stdind,Stdcour,Stdpro1
from portal.models.studentinfo import Student
from portal.models.courses import Courses
from portal.models.stdappli import Stdappli
from datetime import date
from portal.models.offer import Offerletter
from django.views import View
def stu_saved(request):
    return render(request,'student_portal/saved.html')
def stu_support(request):
    return render(request,'student_portal/support.html')
def stu_home(request):
    return render(request,'student_portal/index.html')
def stu_profile(request):
    return render(request,'student_portal/profile.html')
def stu_settings(request):
    return render(request,'student_portal/student_settings.html')
def testoverview(request):
    return render(request,'test_overview.html')
def stu_overview(request,name="a"):
    if(name=="a"):
        print("lknfkenw;fheliufhlierjfiehflrjnckjdcljerbfkjhrbf")
        stdacd=Stdacd.objects.filter(Email=request.session['Email1'])
        stdpro=Stdpro.objects.filter(Email=request.session['Email1'])
        stdind=Stdind.objects.filter(Email=request.session['Email1'])
        stdcour=Stdcour.objects.filter(Email=request.session['Email1'])
        stdpro1=Stdpro1.objects.filter(Email=request.session['Email1'])
        


        data={'stdacd':stdacd,'stdpro':stdpro,'stdind':stdind,'stdcour':stdcour,'stdpro1':stdpro1}

        return render(request,'student_portal/student_overview.html',data)
    else:
        student=Student.objects.get(Firstname=name)
        stdacd=Stdacd.objects.filter(Email=student.Email)
        stdpro=Stdpro.objects.filter(Email=student.Email)
        stdind=Stdind.objects.filter(Email=student.Email)
        stdcour=Stdcour.objects.filter(Email=student.Email)
        stdpro1=Stdpro1.objects.filter(Email=student.Email)

        data={'stdacd':stdacd,'stdpro':stdpro,'stdind':stdind,'stdcour':stdcour,'stdpro1':stdpro1}
        try:
            if(request.session['Email']):
                return render(request,'std_univ.html',data)
        except:
            return render(request,'super_admin/ad_std.html',data)
class stu_search(View):
    def get(self,request,name="a"):
        data={}
        if(name=="a"):
            total_univs=University.objects.all()
        else:
            search=Univcon.objects.filter(Location__icontains=name)
            total_univs=University.objects.all()
            list3=[]
            for i in total_univs:
                for j in search:
                    if(i.Email==j.Email):
                        list3.append(i)
            total_univs=list3
        data['search']=total_univs
        return render(request,'student_portal/search.html',data)
        
    def post(self,request):
        search=request.POST.get('search')
        country=request.POST.get('country')
        feerange=request.POST.get('feerange')

        rankrange1=request.POST.get('rankrange1')
        rankrange2=request.POST.get('rankrange2')
        courses=request.POST.get('courses')
        print(country,rankrange1,courses)
        data={}
        print(search)
        if(search):
            total_univs=University.objects.filter(Firstname__icontains=search)
        elif(country):
            print("yeah elif happening")
            search=Univcon.objects.filter(Location__icontains=country)
            cour_list=Courses.objects.filter(Name=courses)
            #rankrange=Univdetail.objects.filter(Rank>rankrange1).filter(Rank<=rankrange2)
            rankrange1=int(rankrange1)
            rankrange2=int(rankrange2)
            for i in range(int(rankrange1),int(rankrange2+1)):
                if(Univdetail.objects.filter(Rank__icontains=i)):
                    rankrange=Univdetail.objects.filter(Rank__icontains=i)
        
            list=[]
            list2=[]
            list3=[]
            for coun_record in search:
                for cour_record in cour_list:
                    if(coun_record.Email==cour_record.Email):
                        list.append(coun_record)
            for coun_record in list:
                for rank_record in rankrange:
                    if(coun_record.Email==rank_record.Email):
                        list2.append(coun_record)

            total_univs=University.objects.all()
            print("yeah elif happening")
            for i in total_univs:
                for j in list2:
                    if(i.Email==j.Email):
                        list3.append(i)
            total_univs=list3
        else:
            print("in else")
            total_univs=University.objects.all()
            print("taking total univs done")
        
        data['search']=total_univs
        return render(request,'student_portal/search.html',data)
def stu_applied(request):
    stddetail=Stdappli.objects.filter(stdmail=request.session['Email1'])
    print(stddetail)
    data={}
    data['stddetail']=stddetail
    return render(request,'student_portal/applied.html',data)
def personal_details(request):
    return render(request,'student_portal/Personal_details.html')
def professional(request):
    return render(request,'student_portal/professional_qualification.html')
def academic(request):
    return render(request,'student_portal/Academic _Details.html')
def password(request):
    return render(request,'student_portal/Password_security.html')
def preference(request):
    return render(request,'student_portal/Course_application.html')
def course_overview(request):
    return render(request,'student_portal/Course_Overview.html')
def progressbar(request,name="a"):
    if(name!='a'):
        today = date.today()
        stddetail=Stdappli.objects.filter(stdmail=request.session['Email1']).get(univname=name)
        offer=Offerletter.objects.filter(Email=stddetail.univmail).get(Name=request.session['Firstname1'])
        data=offer.Letter
        if(stddetail.status=="accept"):
            d2 = today.strftime("%B %d, %Y")
            ans=100
            a="Application initiated, Processed , Accepted , Happei learing "
        elif(stddetail.status=="reject"):
            d2 = today.strftime("%B %d, %Y")
            ans=60
            a="Application initiated,Processed,Rejected"
        elif(stddetail.status=="applied"):
            d2 = today.strftime("%B %d, %Y")
            ans=30
            a="Application initiated"
        a=a.split(",")      
        return render(request,'student_portal/Progressbar.html',{'ans':ans,'univname':name,'a':a,'d2':d2,'data':data})

