from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.renderers import TemplateHTMLRenderer
from . models import pokemon as PokemonModel
from . serializers import pokemonSerializer


class pokemon(APIView):                  # inherits from an APIView

    def get(self, request):
        obj = PokemonModel.objects.all()      # Getting all values
        serializer = pokemonSerializer(obj, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data             # Data passed in body
        serializer = pokemonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()           # to do post request
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)  # if error


class PokemonDetail(generics.RetrieveAPIView):
    """
    A view that returns a templated HTML representation of a given pokemon.
    """
    queryset = PokemonModel.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'pokemon': self.object}, template_name='pokemon/pokemon_detail.html')
