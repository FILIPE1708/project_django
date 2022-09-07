from django.db import models
from .temporada import Temporada

class Episodio(models.Model):
    nome = models.CharField(max_length=50)
    numero = models.IntegerField()
    Temporada = models.ForeignKey(Temporada, on_delete=models.PROTECT, blank=True, null=True)