from django.db import models

class Temporada(models.Model):
    numero = models.IntegerField()
    ano_lancamento = models.DateField()
