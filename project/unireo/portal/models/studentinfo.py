from django.db import models
from django.core.validators import MinLengthValidator

class Student(models.Model):
    Firstname= models.CharField(max_length=500)
    Phonenumber=models.CharField(max_length=500,null=True)
    Email = models.EmailField()
    Password = models.CharField(max_length=500,null=True)
    Confirmpassword = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.Firstname
    def register(self):
        self.save()

    @staticmethod
    def get_student_by_email(Email):
        try:
            #print(Email)
            #print(Student.objects.all())
            #print(Student.objects.get(Email=Email))
            return Student.objects.get(Email=Email)
        except:
            return False

    def IsExists(Email):
        if Student.objects.filter(Email=Email) :
            return True

        return False