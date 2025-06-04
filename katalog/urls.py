from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zanry/', views.zanry, name='zanry'),
    path('interpreti/', views.interpreti, name='interpreti'),
path('zanr/<int:zanr_id>/', views.detail_zanru, name='detail_zanru'),
path('interpret/<int:interpret_id>/', views.detail_interpreta, name='detail_interpreta'),
]
