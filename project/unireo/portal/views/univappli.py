from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from portal.models.universityinfo import University
from portal.models.application import Application
from django.core.files.storage import FileSystemStorage

class Univappli(View):
    def get(self,request):
        Email=request.session['Email']
        qwe=Application.get_uniapp_by_email(Email)
        if(qwe):
            print(qwe.Prodoc)
            data={}
            listadmpro=qwe.Admpro.split(',')
            listadmpro[0]=listadmpro[0][1:]
            listadmpro[-1]=listadmpro[-1][0:-1]
            for i in range(0,len(listadmpro)):
                if(i!=0):
                    listadmpro[i]=listadmpro[i][2:-1]
                else:
                    listadmpro[i]=listadmpro[i][1:-1]

            listperdoc=qwe.Perdoc.split(',')
            listperdoc[0]=listperdoc[0][1:]
            listperdoc[-1]=listperdoc[-1][0:-1]
            for i in range(0,len(listperdoc)):
                if(i!=0):
                    listperdoc[i]=listperdoc[i][2:-1]
                else:
                    listperdoc[i]=listperdoc[i][1:-1]

            listprodoc=qwe.Prodoc.split(',')
            listprodoc[0]=listprodoc[0][1:]
            listprodoc[-1]=listprodoc[-1][0:-1]
            for i in range(0,len(listprodoc)):
                if(i!=0):
                    listprodoc[i]=listprodoc[i][2:-1]
                else:
                    listprodoc[i]=listprodoc[i][1:-1]


            listacdpro=qwe.Acdpro.split(',')
            listacdpro[0]=listacdpro[0][1:]
            listacdpro[-1]=listacdpro[-1][0:-1]
            for i in range(0,len(listacdpro)):
                if(i!=0):
                    listacdpro[i]=listacdpro[i][2:-1]
                else:
                    listacdpro[i]=listacdpro[i][1:-1]


            listterm=qwe.Term.split(',')
            listterm[0]=listterm[0][1:]
            listterm[-1]=listterm[-1][0:-1]
            for i in range(0,len(listterm)):
                if(i!=0):
                    listterm[i]=listterm[i][2:-1]
                else:
                     listterm[i]=listterm[i][1:-1]

            

            value={'Applyfee':qwe.Applyfee,'Duration':qwe.Duration,'Currency':qwe.Currency,'Admpro':listadmpro,'Amount':qwe.Amount,'Acdpro':listacdpro,
            'Perdoc':listperdoc,'Prodoc':listprodoc,'Term':listterm, 'Upload':qwe.Upload}
            data['value']=value
            return render(request,'ApplicationForm.html',data)
        else:
            return render(request,'ApplicationForm.html')
    def post(self,request):
        Applyfee= request.POST.get('Applyfee')
        Duration=request.POST.get('Duration')
        Currency=request.POST.get('Currency') 
        Amount=request.POST.get('Amount') 
        Admpro=request.POST.getlist('Admpro[]')
        Perdoc=request.POST.getlist('Perdoc[]')
        Acdpro=request.POST.getlist('Acdpro[]')
        Prodoc=request.POST.getlist('Prodoc[]')
        Term=request.POST.getlist('Term[]')
        Upload=request.FILES['Upload']
        fs=FileSystemStorage()
        name=fs.save(Upload.name,Upload)
        url=fs.url(name)
        Email=request.session['Email']
        application=Application(Applyfee=Applyfee,Duration=Duration,Currency=Currency,Amount=Amount,Acdpro=Acdpro,Admpro=Admpro,
        Perdoc=Perdoc , Prodoc=Prodoc,Term=Term, Upload=Upload,Email=Email)
        application.register()
        data={}
        value={'Applyfee':Applyfee,'Duration':Duration,'Currency':Currency,'Amount':Amount,'Acdpro':Acdpro,'Admpro':Admpro,
        'Perdoc':Perdoc,'Prodoc':Prodoc,'Term':Term, 'Upload':Upload}
        data['value']=value
        return render(request,'ApplicationForm.html',data)
