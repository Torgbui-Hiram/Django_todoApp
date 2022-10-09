from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from todo_webApp.models import List
from django.contrib import auth
from . forms import RegisterUserForm

# Register user


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, ('Registration Successful'))
            return redirect('home')

    else:
        form = RegisterUserForm()
    return render(request, 'members/register.html', {'form': form, })


# Login user and authentication
def access_granting(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, (f'Hi {username} welcome to your todo list!'))
            return redirect('home')
        else:
            messages.success(request, ('''
            Sorry your username or password does not match!.
            Please enter a valid username or password and try again
            Thank you'''))
            return redirect('granted',)
    else:
        all_item = List.objects.all()
        form = UserCreationForm()
        return render(request, 'members/login.html', {'form': form})


# Logout user
def logout_user(request):
    messages.success(request, ('Logout successful!'))
    logout(request)
    return redirect('/')
