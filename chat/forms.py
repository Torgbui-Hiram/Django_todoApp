from django import forms
from django.forms import ModelForm
from todo_webApp.models import Room


class ChartForm(ModelForm):
    class Meta:
        model = Room
        fields = ('user_name', 'room_name')
