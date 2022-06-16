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
    doc_externo = open("C:\\Users\\d-sko\\Desktop\\pag\\PRUEBA\\index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)


def base(request):
    return render(request, 'index.html')
    
def base2(request):
    return render(request, '__base.html')


def hello_pokemon(requests):
    context = {
        'pokemon': get_pokemon()
    }
    return render(requests, '__base.html', context)

