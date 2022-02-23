from django.shortcuts import render
from .forms import PhoneNumberForm1, PhoneNumberForm2

# Create your views here.


def form_api_demo(request):
    return render(request, 'core/form_api_demo.html', {'form': PhoneNumberForm1()})


def model_form_demo(request):
    print(PhoneNumberForm2())
    return render(request, 'core/model_form_demo.html', {'form': PhoneNumberForm2()})
