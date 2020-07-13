from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class library(models.Model):
    content= models.TextField()
    author=models.TextField(default='')
    date= models.DateField(("Date"),default=datetime.date.today) 
    user= models.ForeignKey(User,on_delete= models.CASCADE,)

