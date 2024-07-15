from django.shortcuts import render

from .utils import verificar_supresion_de_datos  # Aquí es donde colocarás tu función

def bienvenida(request):
    return render(request, 'bienvenida.html')

def salir_de_veraz(request):
    verificar_supresion_de_datos()  # Llama a tu función aquí
    return render(request, 'salir_de_veraz.html')

def contactar_abogado(request):
    return render(request, 'contactar_abogado.html')

