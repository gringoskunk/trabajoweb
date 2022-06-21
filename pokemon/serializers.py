from rest_framework import serializers
from .models import pokemon
# Name the class as (model name + 'Serializer')


class pokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = pokemon
        fields = '__all__'
