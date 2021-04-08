from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import *
from .models import UserReg
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

# hello

def logoutUser(request):
	logout(request)
	return redirect('main/')

def loginForm(request):
	if request.user.is_authenticated:
		return redirect('home/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home/')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'cebsApp/login.html', context)

       
def main(request):
    return render(request,'cebsApp/frontpage.html')

@login_required(login_url='login')
def orderhistory(request):
    return render(request,'cebsApp/orderhistory.html')

@login_required(login_url='login')
def profile(request):
    return render(request,'cebsApp/profile.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home/')
    else:
        form=CreateUserForm()
        if request.method=='POST':
            if request.POST.get('username') and request.POST.get('email') and request.POST.get('password1'):
                form=CreateUserForm(request.POST)
                x=UserReg()
                if form.is_valid():
                    form.save()
                    x.uname=request.POST.get('username')
                    x.uemail=request.POST.get('email')
                    x.pwd=request.POST.get('password1')
                    x.save()
                    user=form.cleaned_data.get('username')
                    messages.success(request,'Account was created for '+user)
                    return redirect('login/')
        context={'form':form}
        return render(request,'cebsApp/signup.html',context)

@login_required(login_url='login')
def usercart(request):
    return render(request,'cebsApp/usercart.html')

@login_required(login_url='login')
def productdetails(request):
    return render(request,'cebsApp/productdetails.html')

@login_required(login_url='login')
def home(request):
    return render(request,'cebsApp/homepage.html')





