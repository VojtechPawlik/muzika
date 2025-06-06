from django import forms
from .models import Album, Interpret, Zanr

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nazev', 'interpret', 'zanr', 'rok_vydanni', 'obrazek']
        widgets = {
            'nazev': forms.TextInput(attrs={'class': 'form-control'}),
            'interpret': forms.Select(attrs={'class': 'form-control'}),
            'zanr': forms.Select(attrs={'class': 'form-control'}),
            'rok_vydanni': forms.NumberInput(attrs={'class': 'form-control'}),
            'obrazek': forms.FileInput(attrs={'class': 'form-control'}),
        }

class InterpretForm(forms.ModelForm):
    class Meta:
        model = Interpret
        fields = ['jmeno', 'popis', 'narozeni', 'zeme_puvodu', 'obrazek', 'zanry']
        widgets = {
            'jmeno': forms.TextInput(attrs={'class': 'form-control'}),
            'popis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'narozeni': forms.NumberInput(attrs={'class': 'form-control'}),
            'zeme_puvodu': forms.TextInput(attrs={'class': 'form-control'}),
            'obrazek': forms.FileInput(attrs={'class': 'form-control'}),
            'zanry': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class ZanrForm(forms.ModelForm):
    class Meta:
        model = Zanr
        fields = ['nazev', 'popis', 'popularita']
        widgets = {
            'nazev': forms.TextInput(attrs={'class': 'form-control'}),
            'popis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'popularita': forms.NumberInput(attrs={'class': 'form-control'}),
        } 