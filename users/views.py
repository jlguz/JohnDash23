from django.shortcuts import render,redirect

from . forms import CreateUserForm
from . decorators import unauthenticated_user

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

@unauthenticated_user
def register(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ user)
                return redirect('login')
            else:
                messages.info(request,'Username or Password is incorrect')   
    context = {'form':form}

    return render(request, 'users/register.html', context=context)

@unauthenticated_user
def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
                
        if user is not None:
            login(request, user)
            messages.success(request,'You are login')
            return redirect('index')
        else:
            messages.info(request,'Username or Password is incorrect')                
            

    context = {}
    return render(request, 'users/my-login.html', context=context)


# user logout

def logoutuser(request):

    logout(request)
    messages.info(request,'You were logout')
    return redirect('login')  