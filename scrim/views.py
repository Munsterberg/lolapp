from django.shortcuts import render
from django.http import HttpResponse


def scrim(request):
    return render(request, 'scrim/scrim.html')
