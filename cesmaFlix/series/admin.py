from django.contrib import admin
from series.models.categoria import Categoria
from series.models.episodio import Episodio
from series.models.temporada import Temporada

admin.site.register(Categoria)
admin.site.register(Episodio)
admin.site.register(Temporada)
