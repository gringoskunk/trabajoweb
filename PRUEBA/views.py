from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from .services import get_pokemon

def saludo(request):
    documento = """<html><body><h1>Hola mundo</h1></body></html>"""
    return HttpResponse("documento")

def despedida(request):
    return HttpResponse("hasta luego")

def index(request):
    return render(request, 'index.html')

def traer_pokemon(requests):
    try:
        pokemon = get_pokemon()
        return render(requests, 'pokemon.html', {'pokemon': pokemon})
    except Exception as e:
        return render(requests, 'pokemon.html', {'pokemon': {'name': 'zapato', 'type': 'Es entero penca, pero es lo que hay'}})

