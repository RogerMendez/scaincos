from django.db import models

class Aula(models.Model):
    nro = models.CharField(max_length=10, verbose_name='Numero de Aula', unique=True)
    def __unicode__(self):
        return self.nro
    def __str__(self):
        return self.nro
    class Meta:
        ordering = ['nro']
        verbose_name_plural = 'Aulas'
        permissions = (
            ('index_aula', 'Index Aulas'),
        )