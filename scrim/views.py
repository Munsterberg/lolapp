from django.shortcuts import render
# from django.http import HttpResponse

from .models import Scrim


def scrim(request):
    latest_scrim_list = Scrim.objects.all()
    return render(request, 'scrim/scrim.html', {'scrims': latest_scrim_list})
