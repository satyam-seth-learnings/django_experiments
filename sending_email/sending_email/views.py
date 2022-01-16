from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')


def email(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        if email and message:
            send_mail(subject='test eamil subject', message=message, from_email='test@email.com',
                      recipient_list=['check@email.com'], fail_silently=False)
            return render(request, 'success.html')
        else:
            return render(request, 'failed.html')
