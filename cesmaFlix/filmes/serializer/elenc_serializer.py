from rest_framework import serializers
from filmes.models.elenco import Elenco

class ElencoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elenco
        fields = ['integrantes']