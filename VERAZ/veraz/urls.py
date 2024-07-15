# tu_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('quiero-salir-de-veraz/', views.salir_de_veraz, name='salir_de_veraz'),
    path('contactar-abogado/', views.contactar_abogado, name='contactar_abogado'),
]
