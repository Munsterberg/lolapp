from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse

from .models import Scrim


def scrim(request):
    latest_scrim_list = Scrim.objects.order_by('-created_at')
    return render(request, 'scrim/scrim.html', {'scrims': latest_scrim_list})


def scrim_detail(request, scrim_id):
    scrim = get_object_or_404(Scrim, pk=scrim_id)
    return render(request, 'scrim/detail.html', {'scrim': scrim})
