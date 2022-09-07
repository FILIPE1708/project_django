from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=50)
