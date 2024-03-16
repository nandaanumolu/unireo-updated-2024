from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from portal.models.eventsinfo import Event
from django.core.files.storage import FileSystemStorage

class addevents(View):
    def get(self,request):
        return render(request,'Addevents.html')
    def post(self,request):
        Ename=request.POST.get('Ename')
        Edate=request.POST.get('Edate')
        Edetails=request.POST.get('Edetails')
        Ephoto=request.FILES["Ephoto"]
        fs=FileSystemStorage()
        name=fs.save(Ephoto.name,Ephoto)
        url=fs.url(name)
        Email=request.session['Email']
        event=Event(Ename=Ename,Edate=Edate,Edetails=Edetails,Ephoto=url,Email=Email)
        event.register()
        
        return render(request,'Addevents.html')
class editevents(View):
    def get(self,request):
        ee=Event.objects.filter(Email=request.session['Email'])
        data={'ee':ee}
        return render(request,'Editevents.html',data)
