from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alba/', views.seznam_alba, name='seznam_alba'),
    path('interpreti/', views.seznam_interpretu, name='seznam_interpretu'),
    path('zanry/', views.seznam_zanru, name='seznam_zanru'),
    path('album/<int:album_id>/', views.detail_alba, name='detail_alba'),
    path('interpret/<int:interpret_id>/', views.detail_interpreta, name='detail_interpreta'),
    path('zanr/<int:zanr_id>/', views.detail_zanru, name='detail_zanru'),
    path('pridat-album/', views.pridat_album, name='pridat_album'),
    path('pridat-interpreta/', views.pridat_interpreta, name='pridat_interpreta'),
    path('pridat-zanr/', views.pridat_zanr, name='pridat_zanr'),
]
