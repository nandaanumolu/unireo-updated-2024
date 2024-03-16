from django.db import models
from django.core.validators import MinLengthValidator

class Application(models.Model):
    Email=models.EmailField()
    Applyfee= models.CharField(max_length=500,null=True)
    Duration=models.CharField(max_length=500,null=True)
    Currency=models.CharField(max_length=500,null=True) 
    Amount=models.CharField(max_length=500,null=True) 
    Admpro=models.CharField(max_length=500,null=True)
    Acdpro=models.CharField(max_length=500,null=True)
    Perdoc=models.CharField(max_length=500,null=True)
    Prodoc=models.CharField(max_length=500,null=True)
    Term=models.CharField(max_length=500,null=True)
    Upload=models.FileField(upload_to="",null=True)

    def __str__(self):
        return self.Email
    def register(self):
        self.save()
        return True
    def get_uniapp_by_email(Email):
            try:
                #print(Application.objects.get(Email=Email))
                return Application.objects.get(Email=Email)
            except:
                False
