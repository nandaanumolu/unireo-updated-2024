from django.db import models
from django.core.validators import MinLengthValidator

class Consultancydetails(models.Model):
    Cname= models.CharField(max_length=50)
    Aid=models.CharField(max_length=500)
    Aadd=models.CharField(max_length=500)
    Email=models.EmailField(max_length=500)
    Bname=models.CharField(max_length=500)
    Accountnumber=models.CharField(max_length=500)
    Branch=models.CharField(max_length=500)
    Ifsccode=models.CharField(max_length=500)

    def _str_(self):
        return self.Cname
    def register(self):
        self.save()

    
