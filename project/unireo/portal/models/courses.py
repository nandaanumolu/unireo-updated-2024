from django.db import models
from django.core.validators import MinLengthValidator

class Courses(models.Model):
    Name=models.CharField(max_length=50,null=True)
    Type=models.CharField(max_length=50,null=True)
    com=models.CharField(max_length=50,null=True)
    Depname=models.CharField(max_length=50,null=True)
    Courseapp=models.CharField(max_length=50,null=True)
    Appauth=models.CharField(max_length=50,null=True)
    Curr=models.CharField(max_length=50,null=True)
    Amo=models.CharField(max_length=50,null=True)
    Sem=models.CharField(max_length=50,null=True)
    Dur=models.CharField(max_length=50,null=True)
    Couover=models.CharField(max_length=50,null=True)
    Sem1=models.CharField(max_length=50,null=True)
    Sem2=models.CharField(max_length=50,null=True)
    Cri=models.CharField(max_length=50,null=True)
    Email=models.EmailField()

    def __str__(self):
        return self.Name
    def register(self):
        self.save()
        return True
    def get_courses_by_email(Email,name):
            #print(Email)
            #print(Stddetail.objects.all())
            #print(Stddetail.objects.get(Email=Email))
            try:
                print("efhujolyujrgdfhjkyutf")
                print(Email)
                print(Courses.objects.all().filter(Email=Email).get(Name=name))

                return Courses.objects.all().filter(Email=Email).get(Name=name)
            except:
                False
    
