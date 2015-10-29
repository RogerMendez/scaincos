from django.contrib import admin
from django.contrib.auth.models import Permission
from usuarios.models import Persona, Administrativo

admin.site.register(Permission)

@admin.register(Persona)
class PersonaOptions(admin.ModelAdmin):
    list_display = ['ci', 'nombre', 'paterno']
    list_filter = ('tipo', 'ci' )

admin.site.register(Administrativo)