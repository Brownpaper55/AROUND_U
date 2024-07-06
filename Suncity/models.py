from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Program(models.Model):
    name= models.CharField(max_length=100, default = None)
    Location= models.CharField(max_length=100, default = None)
    Date= models.DateField(default = None, help_text='year-month-day')
    Dress_code= models.CharField(max_length=100,default = None)
    Description=models.CharField(max_length=250, default= None)
    start_time= models.TimeField(default = None)
    cover_photo= models.ImageField(null=True, blank=True, upload_to='images/')
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, default = None)
   
    

    def __str__(self):
        return self.name