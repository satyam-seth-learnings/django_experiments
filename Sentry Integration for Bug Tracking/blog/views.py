from django.shortcuts import render


def home(req):
    return render(req, "blog/home.html")


def posts(req):
    division_by_zero = 1 / 0
    return render(req, "blog/posts.html")
