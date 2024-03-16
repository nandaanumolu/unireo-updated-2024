from django.db import models
from django.core.validators import MinLengthValidator

class Consultancy(models.Model):
    Firstname= models.CharField(max_length=50)
    Phonenumber=models.CharField(max_length=500)
    Email = models.EmailField()
    Password = models.CharField(max_length=500)
    Confirmpassword = models.CharField(max_length=500)
    Agentid=models.CharField(max_length=50,null=True)

    def _str_(self):
        return self.Firstname
    def register(self):
        self.save()

    @staticmethod
    def get_consultancy_by_email(Email):
        try:
            #print(Email)
            #print(University.objects.all())
            #print(University.objects.get(Email=Email))
            return Consultancy.objects.get(Email=Email)
        except:
            return False

    def IsExists(Email):
        if Consultancy.objects.filter(Email=Email):
            return True

        return False