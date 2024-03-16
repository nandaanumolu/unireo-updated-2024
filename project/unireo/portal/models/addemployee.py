from django.db import models
from django.core.validators import MinLengthValidator

class Addemployee(models.Model):
    Firstname= models.CharField(max_length=500)
    Phonenumber=models.CharField(max_length=500,null=True)
    Roleaccess=models.CharField(max_length=500,null=True)
    Adminmail=models.CharField(max_length=500,null=True)
    Email = models.EmailField()
    Password = models.CharField(max_length=500,null=True)
    Confirmpassword = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.Firstname
    def register(self):
        self.save()