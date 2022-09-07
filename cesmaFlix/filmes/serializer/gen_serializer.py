from rest_framework import serializers
from filmes.models.genero import Genero

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['nome']