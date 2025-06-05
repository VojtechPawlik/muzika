from django.shortcuts import render
from .models import Album, Zanr, Interpret

def index(request):
    alba = Album.objects.all()
    return render(request, 'muzika/index.html', {'alba': alba})

def zanry(request):
    zanry = Zanr.objects.all()
    return render(request, 'muzika/zanry.html', {'zanry': zanry})

def interpreti(request):
    zanry_s_interprety = Zanr.objects.prefetch_related('interpret_set').all()
    # You might also want to pass all interpreters if you need to list those without a genre,
    # or handle genres with no interpreters gracefully in the template.
    # For now, we'll focus on genres that have interpreters.
    # interpreti_bez_zanru = Interpret.objects.filter(zanry__isnull=True)
    return render(request, 'muzika/interpreti.html', {'zanry_s_interprety': zanry_s_interprety})

def detail_zanru(request, zanr_id):
    zanr = Zanr.objects.get(pk=zanr_id)
    return render(request, 'muzika/detail_zanru.html', {'zanr': zanr})

def detail_interpreta(request, interpret_id):
    interpret = Interpret.objects.get(pk=interpret_id)
    return render(request, 'muzika/detail_interpreta.html', {'interpret': interpret})

def detail_alba(request, album_id):
    album = Album.objects.get(pk=album_id)
    return render(request, 'muzika/detail_alba.html', {'album': album})

def alba(request):
    zanry_s_alby = Zanr.objects.prefetch_related('album_set').all()
    return render(request, 'muzika/alba.html', {'zanry_s_alby': zanry_s_alby})
