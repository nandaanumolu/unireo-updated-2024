from django.db import models
from django.core.validators import MinLengthValidator

class University(models.Model):
    Firstname= models.CharField(max_length=500)
    Phonenumber=models.CharField(max_length=500)
    Email = models.EmailField()
    Password = models.CharField(max_length=500)
    Confirmpassword = models.CharField(max_length=500)

    def __str__(self):
        return self.Firstname
    def register(self):
        self.save()

    @staticmethod
    def get_university_by_email(Email):
        try:
            #print(Email)
            #print(University.objects.all())
            #print(University.objects.get(Email=Email))
            return University.objects.get(Email=Email)
        except:
            return False

    def IsExists(Email):
        if University.objects.filter(Email=Email) :
            return True

        return False