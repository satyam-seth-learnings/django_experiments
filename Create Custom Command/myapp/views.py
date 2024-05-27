from django.shortcuts import render, redirect
from django.core.management import call_command
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "myapp/home.html")


@csrf_exempt
def print_message(request):
    if request.method == "POST":
        try:
            call_command("print_message")
            messages.success(request, "Success! Check Terminal")
        except Exception as e:
            messages.error(request, f"Error: {e}")
        return redirect("/")
    else:
        return redirect("/")
