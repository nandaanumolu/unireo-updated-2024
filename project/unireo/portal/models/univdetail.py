from django.db import models
from django.core.validators import MinLengthValidator

class Univdetail(models.Model):
    Type=models.CharField(max_length=50,null=True)
    Name=models.CharField(max_length=50,null=True)
    Year=models.CharField(max_length=50,null=True)
    Rank=models.CharField(max_length=50,null=True)
    Campuses=models.CharField(max_length=50,null=True)
    Departments = models.CharField(max_length=50,null=True)
    Email=models.EmailField()
    Web=models.CharField(max_length=50,null=True)
    About=models.CharField(max_length=50,null=True)
    Upload=models.FileField(upload_to="",null=True)

    def __str__(self):
        return self.Email
    def register(self):
        self.save()
        return True
    @staticmethod

    def get_univdetail_by_email(Email):
            try:
                print("mounish")
                print(Univdetail.objects.get(Email=Email))
                return Univdetail.objects.get(Email=Email)
            except:
                False

class Univcon(models.Model):
    Email=models.EmailField()
    Intakes=models.CharField(max_length=50,null=True)
    Award=models.CharField(max_length=50,null=True)
    Staff=models.CharField(max_length=50,null=True)
    Students=models.CharField(max_length=50,null=True)
    Departments=models.CharField(max_length=50,null=True)
    Location=models.CharField(max_length=50,null=True)

    Link=models.CharField(max_length=50,null=True)
    Face=models.CharField(max_length=50,null=True)
    Insta=models.CharField(max_length=50,null=True)
    Req=models.CharField(max_length=50,null=True)
    Features=models.CharField(max_length=50,null=True)
    Video=models.FileField(upload_to="",null=True)

    def __str__(self):
        return self.Email
    def register(self):
        self.save()
        return True
    @staticmethod

    def get_univcon_by_email(Email):
            #print(Email)
            #print(Stddetail.objects.all())
            #print(Stddetail.objects.get(Email=Email))
            try:
                print(Univcon.objects.get(Email=Email))
                return Univcon.objects.get(Email=Email)
            except:
                False