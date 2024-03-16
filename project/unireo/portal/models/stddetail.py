from django.db import models
from django.core.validators import MinLengthValidator

class Stdind(models.Model):
    
    Firstname= models.CharField(max_length=500,null=True)
    Lastname= models.CharField(max_length=500)
    Dateofbirth=models.CharField(max_length=50,null=True)
    Gender=models.CharField(max_length=50,null=True)
    Maritial=models.CharField(max_length=50,null=True)
    Nationality=models.CharField(max_length=50,null=True)
    Email = models.EmailField()
    Address=models.CharField(max_length=50,null=True)
    City=models.CharField(max_length=50,null=True)
    State=models.CharField(max_length=50,null=True)
    Country=models.CharField(max_length=50,null=True)
    Phonenumber= models.CharField(max_length=50,null=True)
    Agentid= models.CharField(max_length=50,null=True)
    Agentmail= models.EmailField(max_length=50,null=True)
    #sscgrading=(('M','Marks'),('%','Percentage'),('C','CGPA'))
    def __str__(self):
        return self.Firstname
    def register(self):
        self.save()
        return True


    @staticmethod

    def get_stdind_by_email(Email):
            print(Email)
            #print(Stddetail.objects.all())
            #print(Stddetail.objects.get(Email=Email))
            try:
                return Stdind.objects.get(Email=Email)
            except:
                False
class Stdacd(models.Model):
    Email=models.EmailField()
    Sscqual=models.CharField(max_length=50,null=True)
    Sscname=models.CharField(max_length=50,null=True)
    Sscdate=models.CharField(max_length=10,null=True)
    Sscmarks=models.CharField(max_length=10,null=True)
    Sscgrading=models.CharField(max_length=50,null=True)
    SscDoc=models.FileField(upload_to="")
    #Intgrading=(('M','Marks'),('%','Percentage'),('C','CGPA'))
    Intqual=models.CharField(max_length=50,null=True)
    Intname=models.CharField(max_length=50,null=True)
    Intdate=models.CharField(max_length=10,null=True)
    Intmarks=models.CharField(max_length=10,null=True)
    Intgrading=models.CharField(max_length=50,null=True)
    IntDoc=models.FileField(upload_to="")
    #Unigrading=(('M','Marks'),('%','Percentage'),('C','CGPA'))
    Uniqual=models.CharField(max_length=50,null=True)
    Uniname=models.CharField(max_length=50,null=True)
    Unidate=models.CharField(max_length=10,null=True)
    Unimarks=models.CharField(max_length=10)
    Unigrading=models.CharField(max_length=50,null=True)
    UniDoc=models.FileField(upload_to="")
    Unicname=models.CharField(max_length=50,null=True)
    Agentid= models.CharField(max_length=50,null=True)
    Agentmail= models.EmailField(max_length=50,null=True)
    def __str__(self):
        return self.Email
    def register(self):
        self.save()
        return True

    @staticmethod

    def get_stdacd_by_email(Email):
            #print(Email)
            #print(Stddetail.objects.all())
            #print(Stddetail.objects.get(Email=Email))
            try:
                return Stdacd.objects.get(Email=Email)
            except:
                False

class Stdcour(models.Model):
    Email=models.EmailField()
    Applyingfor=models.CharField(max_length=50,null=True)
    Date=models.CharField(max_length=50,null=True)
    pcoun1=models.CharField(max_length=50,null=True)
    pcoun2=models.CharField(max_length=50,null=True)
    pcoun3=models.CharField(max_length=50,null=True)
    pcour4=models.CharField(max_length=50,null=True)
    pcour5=models.CharField(max_length=50,null=True)
    pcour6=models.CharField(max_length=50,null=True)
    Agentid= models.CharField(max_length=50,null=True)
    Agentmail= models.EmailField(max_length=50,null=True)
    Univname= models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.Email
    def register(self):
        self.save()
        return True
    @staticmethod

    def get_stdcour_by_email(Email):
            #print(Email)
            #print(Stddetail.objects.all())
            #print(Stddetail.objects.get(Email=Email))
            try:
                return Stdcour.objects.get(Email=Email)
            except:
                False
class Stdpro(models.Model):
    Email=models.EmailField()
    Testeng=models.CharField(max_length=50,null=True)
    Yeareng=models.CharField(max_length=10,null=True)
    Overallscoreeng=models.CharField(max_length=10,null=True)
    Uploadeng=models.FileField(upload_to="",null=True)
    Urleng=models.CharField(max_length=10,null=True)
    Agentid= models.CharField(max_length=50,null=True)
    Agentmail= models.EmailField(max_length=50,null=True)

    def __str__(self):
        return self.Email
    def register(self):
        self.save()
        return True
    @staticmethod

    def get_stdpro_by_email(Email):
            #print(Email)
            #print(Stddetail.objects.all())
            #print(Stddetail.objects.get(Email=Email))
            try:
                return Stdpro.objects.all().filter(Email=Email)
            except:
                False


class Stdpro1(models.Model):
    Email=models.EmailField()
    Testad=models.CharField(max_length=50,null=True)
    Yearad=models.CharField(max_length=10,null=True)
    Overallscoread=models.CharField(max_length=10,null=True)
    Uploadad=models.FileField(upload_to="",null=True)
    Urlad=models.CharField(max_length=10,null=True)
    Agentid= models.CharField(max_length=50,null=True)
    Agentmail= models.EmailField(max_length=50,null=True)
    
    def __str__(self):
        return self.Email
    def register(self):
        self.save()
        return True
    @staticmethod

    def get_stdpro1_by_email(Email):
            #print(Email)
            #print(Stddetail.objects.all())
            #print(Stddetail.objects.get(Email=Email))
            try:
                return Stdpro1.objects.all().filter(Email=Email)
            except:
                False


    
