from django.contrib import admin
from .models import Album, Zanr, Interpret

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nazev', 'interpret', 'zanr', 'rok_vydanni', 'obrazek')

class InterpretAdmin(admin.ModelAdmin):
    list_display = ('jmeno', 'narozeni', 'zeme_puvodu', 'obrazek')

admin.site.register(Album, AlbumAdmin)
admin.site.register(Zanr) # Zanr does not have an image, so no custom admin needed for it yet
admin.site.register(Interpret, InterpretAdmin)
