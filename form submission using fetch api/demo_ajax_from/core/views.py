from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse 
from .forms import StudentForm

# Create your views here.

def home(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["roll_no"])
            print(form.cleaned_data["name"])
            return JsonResponse({'status':'done','message':'form successfully submitted'})
        return JsonResponse({'status':'invalid','errors':form.errors.get_json_data()})
    else:
        form = StudentForm()
    return render(request, "core/home.html", {"form": form, 'action_url':reverse('home')})
