from django.shortcuts import render


def home(req):
    return render(req, "blog/home.html")


def posts(req):
    return render(req, "blog/posts.html")
