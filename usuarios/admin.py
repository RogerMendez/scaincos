from django.contrib import admin
from django.contrib.auth.models import Permission
from usuarios.models import Persona

admin.site.register(Permission)

@admin.register(Persona)
class UnidadOptions(admin.ModelAdmin):
    list_display = ['ci', 'nombre', 'paterno']
    list_filter = ('ci', )
