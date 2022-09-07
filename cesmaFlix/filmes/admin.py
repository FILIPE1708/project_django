from django.contrib import admin
from filmes.models.genero import Genero
from filmes.models.diretor import Diretor

admin.site.register(Genero)
admin.site.register(Diretor)
