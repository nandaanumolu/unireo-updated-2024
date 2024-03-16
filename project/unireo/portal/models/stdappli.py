from django.db import models
from django.core.validators import MinLengthValidator

class Stdappli(models.Model):
    id=models.CharField(max_length=500,null=False,primary_key=True)
    stdname= models.CharField(max_length=500,null=True)
    univname= models.CharField(max_length=500,null=True)
    stdmail= models.CharField(max_length=500,null=True)
    univmail= models.CharField(max_length=500,null=True)
    date= models.CharField(max_length=500,null=True)
    status= models.CharField(max_length=500,null=True)
    pstatus= models.CharField(max_length=500,null=True)
    program=models.CharField(max_length=500,null=True)
    agentmail=models.CharField(max_length=500,null=True)
    fee=models.CharField(max_length=500,null=True)
    Coursename=models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.stdname
    def register(self):
        self.save()
        return True