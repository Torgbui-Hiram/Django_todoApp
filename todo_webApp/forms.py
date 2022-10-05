from django import forms
from . models import List


class ListForm(forms.ModelForm):
    item = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Add your item to the todo list!'}))
    completed = forms.BooleanField(disabled=True, widget=forms.CheckboxInput(
        attrs={'class': 'form-control'}))
    # user = forms.Select(attrs={'class': 'form-select'})
    # description = forms.Textarea(attrs={'class': 'form-control'})
    created_date = forms.DateTimeField(widget=forms.DateTimeInput(
        attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}))

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
