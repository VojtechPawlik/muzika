from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Zanr, Interpret
from .forms import AlbumForm, InterpretForm, ZanrForm

def index(request):
    alba = Album.objects.all().order_by('-id')[:6]
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
    zanr = get_object_or_404(Zanr, pk=zanr_id)
    return render(request, 'muzika/detail_zanru.html', {'zanr': zanr})

def detail_interpreta(request, interpret_id):
    interpret = get_object_or_404(Interpret, pk=interpret_id)
    return render(request, 'muzika/detail_interpreta.html', {'interpret': interpret})

def detail_alba(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'muzika/detail_alba.html', {'album': album})

def alba(request):
    zanry_s_alby = Zanr.objects.prefetch_related('album_set').all()
    return render(request, 'muzika/alba.html', {'zanry_s_alby': zanry_s_alby})

def seznam_alba(request):
    alba = Album.objects.select_related('interpret', 'zanr').all()
    return render(request, 'muzika/alba.html', {'alba': alba})

def seznam_interpretu(request):
    zanry_s_interprety = Zanr.objects.prefetch_related('interpret_set').all()
    return render(request, 'muzika/interpreti.html', {'zanry_s_interprety': zanry_s_interprety})

def seznam_zanru(request):
    zanry = Zanr.objects.all()
    return render(request, 'muzika/zanry.html', {'zanry': zanry})

def pridat_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('seznam_alba')
    else:
        form = AlbumForm()
    return render(request, 'muzika/pridat_album.html', {'form': form})

def pridat_interpreta(request):
    if request.method == 'POST':
        form = InterpretForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('seznam_interpretu')
    else:
        form = InterpretForm()
    return render(request, 'muzika/pridat_interpreta.html', {'form': form})

def pridat_zanr(request):
    if request.method == 'POST':
        form = ZanrForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seznam_zanru')
    else:
        form = ZanrForm()
    return render(request, 'muzika/pridat_zanr.html', {'form': form})
