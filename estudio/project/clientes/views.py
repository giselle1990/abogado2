from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # Asegúrate de importar User





def index(request):
    return render(request, 'clientes/index.html')

def clientes_list(request):
    # Obtiene todos los usuarios registrados
    usuarios = User.objects.all()
    return render(request, 'clientes/clientes_list.html', {'usuarios': usuarios})

def expedientes(request):
    return render (request, 'clientes/expedientes.html')