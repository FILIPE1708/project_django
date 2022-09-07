from rest_framework.decorators import api_view
from filmes.models.genero import Genero
from filmes.models.diretor import Diretor
from filmes.serializer.gen_serializer import GeneroSerializer
from filmes.serializer.dir_serializer import DiretorSerializer
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
def api_diretor(request):
    if request.method  == 'GET':
        diretores = Diretor.objects.all()
        diretor_serializer = DiretorSerializer(diretores, many=True)

        return Response(
            diretor_serializer.data,
            status=status.HTTP_200_OK
        )

    if request.method == 'POST':
        Diretor.objects.create(
            nome = request.POST.get('nome'),
            obras = request.POST.get ('obras'),
            Genero = request.POST.get ('Genero')
        )

        return Response(status=status.HTTP_201_CREATED)
