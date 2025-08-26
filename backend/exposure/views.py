from django.shortcuts import render
from django.conf import settings


def map_view(request):
    context = {
        'TILES_URL': settings.TILES_URL,
        'API_BASE': settings.API_BASE,
        'ATTRIBUTION': '© OpenStreetMap contributors',
    }
    return render(request, 'exposure/map.html', context)
