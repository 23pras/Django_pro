from django.db import models

# Create your models here.
class Login(models.Model):
    fname=models.CharField(max_length=30)
    userid=models.CharField(max_length=30,unique=True)
    passwd=models.CharField(max_length=30)
    def __str__(self):
        return self.fname
        