from django.db import models
from django.core.validators import MinLengthValidator

class Event(models.Model):
    Ename=models.CharField(max_length=50,null=True)
    Edate=models.CharField(max_length=50,null=True)
    Edetails=models.CharField(max_length=50,null=True)
    Ephoto=models.FileField(upload_to="",null=True)
    Email=models.EmailField(null=True)


    def __str__(self):
        return self.Ename
    def register(self):
        self.save()
        return True

    def getallevents():
        return Event.objects.all()

class Blog(models.Model):
    Bname=models.CharField(max_length=50,null=True)
    Bdate=models.CharField(max_length=50,null=True)  
    Bdetail=models.CharField(max_length=50,null=True)
    Bphoto=models.FileField(upload_to="",null=True)
    Email=models.EmailField(null=True)

    def __str__(self):
        return self.Bname
    def register(self):
        self.save()
        return True

    def getallblogs():
        return Blog.objects.all()
