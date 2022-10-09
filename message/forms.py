from django import forms


class MessageForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter your username here'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter your email here!'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Please enter your message here!'}))

    name.label = ''
    email.label = ''
    message.label = ''
