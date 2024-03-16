from django.db import models
from django.core.validators import MinLengthValidator

class Offerletter(models.Model):
    Letter=models.FileField(upload_to="")
    Name=models.CharField(max_length=500)
    Email=models.EmailField()
    def register(self):
        self.save()
        return True
    def __str__(self):
        return self.Email