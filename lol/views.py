from django.shortcuts import render


def home(request):
    return render(request, "lol/index.html")


def home_files(request, filename):
    return render(request, filename, content_type="text_plain")


def login(request):
    return render(request, "lol/login.html")
