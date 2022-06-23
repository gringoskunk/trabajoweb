from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from . models import planta as PlantaModel
from . serializers import plantaSerializer
from rest_framework.response import Response

# Create your views here.
class planta(APIView):                  # inherits from an APIView

    def get(self, request):
        obj = PlantaModel.objects.all()      # Getting all values
        serializer = plantaSerializer(obj, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data             # Data passed in body
        serializer = plantaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()           # to do post request
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)  # if error
