from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField( "Nombre", max_length=50)
    shor_name = models.CharField("Nombre Corto", max_length=20)
    anulate = models.BooleanField("Anulado", default=False)

    class Meta:
        verbose_name = "Mi departamento"
        verbose_name_plural = "Areas de la empresa"

    def __str__(self):
        return (f"{self.id} - {self.name} - {self.shor_name}")