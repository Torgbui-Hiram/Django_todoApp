from django.shortcuts import render, redirect
from .forms import ChartForm
from django.contrib import messages
from todo_webApp.models import Message, Room


def startchat(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        room_name = request.POST['room_name']
        # Checking if room_name already exist in database
        if Room.objects.filter(room_name=room_name).exists():
            info = f'Room name {room_name} already exist, Use a new name and try again!'
            messages.success(request, message=info)
            return redirect('chat')
        else:
            user_name = request.POST['user_name']
            room_name = request.POST['room_name']
            form = ChartForm({'user_name': user_name, 'room_name': room_name})
            if form.is_valid():
                form.save()
                confirm = f'Your chart name: {user_name} and room: {room_name} is created!'
                messages.success(request, confirm)
            return redirect('chat')
    else:
        return render(request, 'index.html', {})





