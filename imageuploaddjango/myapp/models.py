from django.db import models

# Create your models here.
class MyImage(models.Model):
    fname=models.CharField(max_length=50)
    email=models.EmailField()
    file=models.FileField()
    class Meta:
        db_table='MyImage'