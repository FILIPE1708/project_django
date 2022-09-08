from django.contrib import admin
from filmes.models.genero import Genero
from filmes.models.diretor import Diretor
from filmes.models.elenco import Elenco

admin.site.register(Genero)
admin.site.register(Diretor)
admin.site.register(Elenco)
