from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.CharField(max_length=100, widget=forms.TimeInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your email here!'}))
    first_name = forms.CharField(max_length=30, widget=forms.TimeInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your first name!'}))
    last_name = forms.CharField(max_length=30, widget=forms.TimeInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your last name!'}))

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        # setting the field labels to empty
        self.fields['username'].label = ''
        self.fields['email'].label = ''
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
        widgets = {'username': forms.TextInput(
            attrs={'placeholder': 'Please enter your username'}), }
