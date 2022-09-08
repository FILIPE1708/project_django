from rest_framework.decorators import api_view
from series.models.temporada import Temporada
from series.serializer.temp_serializer import TemporadaSerializer
from series.models.episodio import Episodio
from series.serializer.ep_serializer import EpisodioSerializer
from rest_framework.response import Response
from  rest_framework import status

@api_view(['GET', 'POST'])
def api_temporada(request):
    if request.method  == 'GET':
        temporadas = Temporada.objects.all()
        temporada_serializer = TemporadaSerializer(temporadas, many=True)

        return Response(
            temporada_serializer.data,
            status=status.HTTP_200_OK
        )

    if request.method == 'POST':
        Temporada.objects.create(
            numero = request.POST.get('numero'),
            ano_lancamento = request.POST.get ('ano_lancamento')
        )

        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def api_episodio(request):
    if request.method  == 'GET':
        episodios = Episodio.objects.all()
        episodio_serializer = EpisodioSerializer(episodios, many=True)

        return Response(
            episodio_serializer.data,
            status=status.HTTP_200_OK
        )

    if request.method == 'POST':
        Episodio.objects.create(
            nome = request.POST.get('nome'),
            numero = request.POST.get ('numero'),
            Temporada = request.POST.get ('Temporada')
        )

        return Response(status=status.HTTP_201_CREATED)