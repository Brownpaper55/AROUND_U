from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Program(models.Model):
    name= models.CharField(max_length=100)
    Location= models.CharField(max_length=100)
    Date= models.DateField()
    Dress_code= models.CharField(max_length=100)
    Description=models.CharField(max_length=250)
    start_time= models.TimeField()
    cover_photo= models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username