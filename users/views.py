from django.shortcuts import render,redirect

from . forms import CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

def register(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ user)
                return redirect('login')

    context = {'form':form}

    return render(request, 'users/register.html', context=context)


def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
                
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request,'Usernama or Password is incorrect')                
            

    context = {}
    return render(request, 'users/my-login.html', context=context)


# user logout

def logoutuser(request):

    logout(request)

    return redirect('login')  