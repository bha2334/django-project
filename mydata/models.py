from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class library(models.Model):
    content= models.TextField()
    author=models.TextField(default='')
    date= models.DateField(("Date"),default=datetime.date.today) 
    user= models.ForeignKey(User,on_delete= models.CASCADE,)

class sfile(models.Model):
    tittle=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='desktop/pdf')

    def __str__(self):
        return self.tittle