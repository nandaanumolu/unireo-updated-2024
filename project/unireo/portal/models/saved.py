from django.db import models
from django.core.validators import MinLengthValidator

class Saved(models.Model):
    #Image=models.filefield()
    Universityname=models.CharField(max_length=500)
    About=models.CharField(max_length=500)
    Mail=models.EmailField(null=True)
    Phonenumber=models.CharField(max_length=500,null=True)
    Location=models.CharField(max_length=500,null=True)

    def register(self):
        self.save()
        return True
    def __str__(self):
        return self.Mail