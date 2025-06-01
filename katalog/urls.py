from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zanry/', views.zanry, name='zanry'),
    path('interpreti/', views.interpreti, name='interpreti'),
]
