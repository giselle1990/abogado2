from django.contrib import admin

# Register your models here.
# clientes/admin.py
from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'direccion', 'fecha_registro')
    search_fields = ('nombre', 'email')
