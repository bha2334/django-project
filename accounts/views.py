from django.shortcuts import render,redirect

from django.contrib import auth
from django.contrib.auth.models import User
from mydata.views import show
from .models import extendeduser,update
from  .forms import nameform
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

# bhasha
# bhasha

def login(request):
    if request.method == "POST":
        # check whether user exist
        uname = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate( username =uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect(show)
        else:
            return render (request,'home.html', { 'error':"invalid username or password!!"})

    else:
        return render(request, 'home.html')


def signup(request):
    if request.method =="POST":
         # to create a user
        pw= request.POST['password']
        pw2= request.POST['confirmpassword'] 
        if pw== pw2:
         #if both passwords matched
         # check whether the user exist or not
            try:
               user= User.objects.get(username=request.POST['username'])
               return render( request,'register.html', {'error' : "username exist"})
            except User.DoesNotExist:
                user=User.objects.create_user(username= request.POST['username'],password= request.POST['password'])
                uname=request.POST['username']
                phnum=request.POST['phone']
                age=request.POST['age']
                email=request.POST['email']
                newextendeduser=extendeduser(uname=uname,phone_num=phnum,age=age,email=email,user=user)
                newextendeduser.save()
                auth.login(request,user)
                #return HttpResponse("Signed up")
                return render(request,'udashboard.html')
        else:
            return render( request,'register.html', { 'error' : "Passwords not matched"})
    else:
        return render(request,'register.html')  

def logout(request):
    auth.logout(request)
    return redirect(home)

@login_required(login_url='/login/')
def display(request):
    datas=extendeduser.objects.filter(user=request.user)
    return render(request,"showdata.html",{'data':datas})

def edit(request, template_name="edit.html"):
    if request.method == "POST":
        uname=request.POST['username']
        phnum=request.POST['phone']
        age=request.POST['age']
        email=request.POST['email']
        user=request.user
        newupdate=extendeduser(uname=uname,phone_num=phnum,age=age,email=email,user=user)
        newupdate.save()
        return render( request,'udashboard.html')
    else:
        return render( request,'edit.html')
            
   