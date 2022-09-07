from rest_framework import serializers
from series.models.episodio import Episodio

class EpisodioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodio
        fields = ['nome', 'numero', 'Temporada']