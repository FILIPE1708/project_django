from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from series.models.temporada import Temporada
from series.serializer.temp_serializer import TemporadaSerializer
from series.models.episodio import Episodio
from series.serializer.ep_serializer import EpisodioSerializer


class api_temporada(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Temporada.objects.all()
    serializer_class = TemporadaSerializer


class api_episodio(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Episodio.objects.all()
    serializer_class = EpisodioSerializer