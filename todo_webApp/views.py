from django.shortcuts import render, redirect
from . forms import ListForm
from .models import List
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# index page function


def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_item = List.objects.all()
            messages.success(request, ("Your item was added succesfully"))
            completed = True
            return redirect('home')
        else:
            messages.success(
                request, ("Please there was an error with your form."))
            return render(request, 'webApp/index.html', {'form': form, })
    else:
        all_item = List.objects.all()
        form = ListForm()
        return render(request, 'webApp/index.html', {'form': form, 'all_item': all_item, })


# show item selecte function
def show_item(request, id):
    selected = False
    item = List.objects.get(pk=id)
    return render(request, 'webApp/show_item.html', {'item': item, })


# Deleted todo item function
def delete_item(request, id):
    item = List.objects.get(pk=id)
    item.delete()
    messages.success(request, ('item has been deleted'))
    return redirect('home')


# crossing off item function
def cross_off(request, id):
    item = List.objects.get(pk=id)
    item.completed = True
    item.save()
    return redirect('home')


# Uncrossing function
def uncross(request, id):
    item = List.objects.get(pk=id)
    item.completed = False
    item.save()
    return redirect('home')


# Editing selected item function
def edit_item(request, id):
    if request.method == 'POST':
        item = List.objects.get(pk=id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid:
            form.save()
            messages.success(request, (f'Item was edited to {item.item}.'))
            return redirect('home')
    else:
        item = List.objects.get(pk=id)
        form = ListForm(request.POST or None, instance=item)
        return render(request, 'webApp/edit.html', {'item': item, 'form': form})


# add item to list
def add_item(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Your item was added succesfully"))
            completed = True
            return redirect('home')
    else:
        form = ListForm(request.POST or None)
        return render(request, 'webApp/add_item.html', {'form': form})


# Register user
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
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
        form = UserCreationForm()
    return render(request, 'webApp/register.html', {'form': form, })


# Login user and authentication
def user_login(request):
    if request.method == "POST":
        all_item = List.objects.all()
        form = UserCreationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'webApp/index.html', {'all_item': all_item, })
        else:
            messages.success(request, ('Sorry try again.'))
            return redirect('register',)
    else:
        form = UserCreationForm()
        return render(request, 'webApp/login_user.html', {'form': form, })


# Logout user
def logout_user(request):
    logout(request)
    messages.success(request, ('Logout successful!'))
    return redirect('home')
