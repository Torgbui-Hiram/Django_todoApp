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
