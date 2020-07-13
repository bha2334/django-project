from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class extendeduser(models.Model):
    uname=models.CharField(max_length=100,default='')
    phone_num= models.CharField(max_length=15)
    age= models.IntegerField()
    email=models.CharField(max_length=100,default='')
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class update(models.Model):
    phone_num= models.CharField(max_length=15)
    age=models.IntegerField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)