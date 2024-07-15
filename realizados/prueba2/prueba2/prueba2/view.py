from curses import nocbreak
from django.http import HttpResponse
import datetime

def saludo(request): 
    return HttpResponse ("holiii")

def saludo2(request):
    nombre = input("Ingresa tu nombre: ")
    return HttpResponse(f"hola {nombre}")

def nombre(request, nombre: str, apellido: str):
    return HttpResponse(f"{apellido.upper()}, {nombre}")

def damefecha(request):
    fecha_actual = datetime.datetime.now()
    documento= """<html>
    <body>
    <h1>
    fecha y hora %s 
    <html>
    <body>
    <h1>
    <html>""" % fecha_actual
    return HttpResponse(documento)



