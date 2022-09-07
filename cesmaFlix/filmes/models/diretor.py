from django.db import models
from .genero import Genero

class Diretor(models.Model):
    nome = models.CharField(max_length=50)
    obras = models.TextField()
    Genero = models.ManyToManyField(Genero)