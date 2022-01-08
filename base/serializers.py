from . models import Movies
from rest_framework import serializers

class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields='__all__'