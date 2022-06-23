from rest_framework import serializers
from .models import planta
# Name the class as (model name + 'Serializer')


class plantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = planta
        fields = '__all__'
