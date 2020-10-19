from django.shortcuts import render,redirect
from .models import library, sfile
from django.contrib.auth.models import User

from .forms import BookForm
# Create your views here.
def show(request):
    log_user= request.user
    mylib=library.objects.filter(user=log_user)
    return render(request, 'udashboard.html',{'m':mylib}) 

def upload(request):
    if request.method=='POST':
        form= BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('showall')
    else:
        form=BookForm
        return render(request,'upload.html',{'form':form})

def showall(request):
    mylib=sfile.objects.all()
    return render(request,'showall.html',{'m':mylib})

