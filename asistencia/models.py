from django.db import models

from usuarios.models import Persona

class Asistencia(models.Model):
    fecha = models.DateField(auto_now_add=True)
    entrada = models.TimeField(blank=True, null=True, verbose_name="Hora Entrada Mañana")
    salida = models.TimeField(blank=True, null=True, verbose_name="Hora Salida Mañana")
    horas_realizadas = models.TimeField(blank=True, null=True, default="00:00")
    atraso = models.TimeField(blank=True, null=True)
    persona = models.ForeignKey(Persona)
    def __str__(self):
        return self.persona.nombre
    def __unicode__(self):
        return self.persona.nombre
    class Meta:
        verbose_name_plural = "Asistencia"
        ordering = ['fecha']
        permissions=(
            ("detail_asistencia", "Detalle Asistencia"),
            ("detail_fecha_asistencia", "Asistencia Por Fecha"),
            ("historial_month_asistencia", "Historial Mensual"),
            ("historial_year_asistencia", "Historial Anual"),
        )