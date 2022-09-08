from rest_framework.decorators import api_view
from filmes.models.genero import Genero
from filmes.models.elenco import Elenco
from filmes.serializer.gen_serializer import GeneroSerializer
from filmes.serializer.elenc_serializer import ElencoSerializer
from rest_framework.response import Response
from  rest_framework import status

@api_view(['GET', 'POST'])
def api_genero(request):
    if request.method  == 'GET':
        generos = Genero.objects.all()
        genero_serializer = GeneroSerializer(generos, many=True)

        return Response(
            genero_serializer.data,
            status=status.HTTP_200_OK
        )

    if request.method == 'POST':
        Genero.objects.create(
            nome = request.POST.get('nome')
        )

        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def api_elenco(request):
    if request.method  == 'GET':
        elencos = Elenco.objects.all()
        elenco_serializer = ElencoSerializer(elencos, many=True)

        return Response(
            elenco_serializer.data,
            status=status.HTTP_200_OK
        )

    if request.method == 'POST':
        Elenco.objects.create(
            integrantes = request.POST.get('integrantes'),
        )

        return Response(status=status.HTTP_201_CREATED)
