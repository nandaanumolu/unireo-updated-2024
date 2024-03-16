from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from portal.models.courses import Courses
from portal.models.universityinfo import University
class courses(View):
    def get(self,request):
        return render(request,'Courses.html')
    
    def post(self,request):
        Name=request.POST.get('Name')
        Type=request.POST.get('Type')
        Depname=request.POST.get('Depname')
        Courseapp=request.POST.get('Courseapp')
        Appauth=request.POST.get('Appauth')
        Curr=request.POST.get('Curr')
        Amo=request.POST.get('Amo')
        Sem=request.POST.get('Sem')
        Dur=request.POST.get('Dur')
        Couover=request.POST.get('Couover')
        Sem1=request.POST.getlist('Sem1[]')
        Sem2=request.POST.getlist('Sem2[]')
        Cri=request.POST.getlist('Cri[]')
        Email=request.session['Email']

        newcourse=Courses(Name=Name,Type=Type,Depname=Depname,Courseapp=Courseapp,Appauth=Appauth,
        Curr=Curr,Amo=Amo,Sem=Sem,Dur=Dur,Couover=Couover,Sem1=Sem1,Sem2=Sem2,Cri=Cri,Email=Email)
        try:
            checkingforexistance=Courses.objects.filter(Email=Email).get(Name=Name)
            if(checkingforexistance):
                checkingforexistance.delete()
        except:
            pass
        newcourse.register()
        saved=Courses.objects.filter(Email=request.session['Email'])
        print("guru")
        #print(saved)
        for i in saved:
            print(i.Name)
        return render(request,'Courses.html')
class savedcourses(View):
    def get(self,request,name="a",name1="b"):
        if(name=="a"):
            saved=Courses.objects.filter(Email=request.session['Email'])
            print("guru")
            #print(saved)
            data={'saved':saved}
            return render(request,'CourseCards.html',data)
        elif(name1=="delete"):
             saved=Courses.objects.filter(Email=request.session['Email']).filter(Name=name)

             
             saved.delete()
             return redirect('savedcourses')
        elif(name1=="edit"):
            print("hiiiiiii")
            data={}
            print(request.session['Email'])
            university= University.get_university_by_email(request.session['Email'])

            print(university.Email)
            qwe="rty"
            print(qwe)
            if(university):
                univcourses=Courses.get_courses_by_email(university.Email,name)
                print(univcourses)
            
            if(univcourses):
                listsem1=univcourses.Sem1.split(',')
                listsem1[0]=listsem1[0][1:]
                listsem1[-1]=listsem1[-1][0:-1]
                for i in range(0,len(listsem1)):
                    if(i!=0):
                        listsem1[i]=listsem1[i][2:-1]
                    else:
                        listsem1[i]=listsem1[i][1:-1]
                listsem2=univcourses.Sem2.split(',')
                listsem2[0]=listsem2[0][1:]
                listsem2[-1]=listsem2[-1][0:-1]
                for i in range(0,len(listsem2)):
                    if(i!=0):
                        listsem2[i]=listsem2[i][2:-1]
                    else:
                        listsem2[i]=listsem2[i][1:-1]
                listcri=univcourses.Cri.split(',')
                listcri[0]=listcri[0][1:]
                listcri[-1]=listcri[-1][0:-1]
                for i in range(0,len(listcri)):
                    if(i!=0):
                        listcri[i]=listcri[i][2:-1]
                    else:
                        listcri[i]=listcri[i][1:-1]

                print(univcourses.Courseapp)
                print(univcourses.Amo)
                print(univcourses.Couover)


                value={'Name':univcourses.Name,'Type':univcourses.Type,'Depname':univcourses.Depname,'Courseapp':univcourses.Courseapp,'Appauth':univcourses.Appauth,
                'Curr':univcourses.Curr,
                'Amo':univcourses.Amo,'Sem':univcourses.Sem,'Dur':univcourses.Dur,'Couover':univcourses.Couover,'Sem1':listsem1,
                'Sem2':listsem2,'Dur':univcourses.Dur,
                'Cri':listcri,'Email':univcourses.Email}
                data={'value':value}
                return render(request,'Courses.html',data)
        
class coursesoverview(View):
    def get(self,request,name="a"):
        univcourses=Courses.objects.get(Name=name)
        #print(univcourses)
        print('guru')
        saved=Courses.objects.filter(Name=univcourses.Name)
        data={'saved':saved}
        return render(request,'CourseOverview.html',data)
 