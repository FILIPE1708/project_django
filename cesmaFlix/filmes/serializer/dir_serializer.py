from rest_framework import serializers
from filmes.models.diretor import Diretor

class DiretorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diretor
        fields = ['nome', 'obras', 'Genero']