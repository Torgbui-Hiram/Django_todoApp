from django.shortcuts import render


def startchat(request):
    return render(request, 'index.html', {})
