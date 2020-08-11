from django.shortcuts import render
from .models import library
from django.contrib.auth.models import User

# Create your views here.
def show(request):
    log_user= request.user
    mylib=library.objects.filter(user=log_user)
    return render(request, 'udashboard.html',{'m':mylib}) 

def add(request):
    if request.method=='POST':
        data= request.POST['bookname']
        author=request.POST['authorname']
        new= library(content=data,author=author,user=request.user)
        new.save()
        return render(request,'addbook.html')
    else:
        return render(request,'addbook.html')

def showall(request):
    mylib=library.objects.all()
    return render(request,'showall.html',{'m':mylib})

