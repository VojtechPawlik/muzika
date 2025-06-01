from django.shortcuts import render
from .models import Album, Zanr, Interpret

def index(request):
    alba = Album.objects.all()
    return render(request, 'muzika/index.html', {'alba': alba})

def zanry(request):
    zanry = Zanr.objects.all()
    return render(request, 'muzika/zanry.html', {'zanry': zanry})

def interpreti(request):
    interpreti = Interpret.objects.all()
    return render(request, 'muzika/interpreti.html', {'interpreti': interpreti})
