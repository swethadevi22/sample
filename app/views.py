from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
def home(request):
   return render(request, 'home.html')
def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'your account has created')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    context={'form':form}
    return render(request,'register.html',context)
def login(request):
    return render(request,'login.html')
def logout(request):
    return render (request,'logout.html')



# Create your views here.
