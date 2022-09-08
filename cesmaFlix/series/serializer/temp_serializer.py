from rest_framework import serializers
from series.models.temporada import Temporada

class TemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporada
        fields = ['numero', 'ano_lancamento']