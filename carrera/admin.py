from django.contrib import admin

from carrera.models import Carrera, Materia

@admin.register(Carrera)
class CarreraOptions(admin.ModelAdmin):
    list_display = ['nombre', 'tiempo']
    list_filter = ('tiempo', )