from django.db import models
from django.core.validators import MinLengthValidator

class Employee(models.Model):
    Empname=models.CharField(max_length=50,null=True)
    Empdesg=models.CharField(max_length=50,null=True)
    Empphone=models.CharField(max_length=50,null=True)
    Empmail=models.EmailField(max_length=50,null=True)
    Emppassword=models.CharField(max_length=50,null=True)
    Empconfirmpassword=models.CharField(max_length=50,null=True)
    Univmail=models.EmailField(max_length=50,null=True)


    def __str__(self):
        return self.Empname
    def register(self):
        self.save()
        return True
    @staticmethod
    def get_employee_by_email(Empmail):
        try:
            return Employee.objects.get(Empmail=Empmail)
        except:
            return False
