from django import forms
from . models import List
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


class ListForm(forms.ModelForm):
    item = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter title of your plan here!'}))
    completed = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form-control'}))
    user = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter username here!'}))
    # description = forms.Textarea(attrs={'class': 'form-control'})
    created_date = forms.DateTimeField(widget=forms.DateTimeInput(
        attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}))

    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        self.fields['item'].label = ''
        self.fields['completed'].label = ''
        self.fields['user'].label = ''
        self.fields['created_date'].label = ''

    class Meta:
        model = List
        fields = ['item', 'completed', 'user', 'description', 'created_date']
        labels = {'item': '',
                  'completed': '',
                  'user': '',
                  'description': '',
                  'created_date': '', }
        widgets = {'description': forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Please enter some details about your todo item!'}),
            'user': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select user', })}
