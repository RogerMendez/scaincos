from django.db import models

# Create your models here.
class ExcelNotas(models.Model):
    excel = models.FileField(upload_to='notas/%Y/%m/%d')