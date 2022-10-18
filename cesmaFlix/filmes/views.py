from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from filmes.models.genero import Genero
from filmes.models.elenco import Elenco
from filmes.serializer.gen_serializer import GeneroSerializer
from filmes.serializer.elenc_serializer import ElencoSerializer


class api_genero(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class api_elenco(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Elenco.objects.all()
    serializer_class = ElencoSerializer