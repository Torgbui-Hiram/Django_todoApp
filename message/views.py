from django.shortcuts import render, redirect
from .forms import MessageForm
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_email(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            html = render_to_string(
                'message/emails/contact.html', {'name': name,
                                                'email': email,
                                                'message': message})
            send_mail('okito', 'This is the message', 'hiramkumado@gmail.com',
                      ['rigik11251@zuperar.com'], html_message=html)
            return redirect('send')
    else:
        form = MessageForm()
        return render(request, 'message/mailSend.html', {'form': form})
