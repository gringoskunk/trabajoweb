from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context


def saludo (request):
    documento="""<html><body><h1>Hola mundo</h1></body></html>"""
    return HttpResponse("documento")

def despedida(request):
    return HttpResponse("hasta luego")

def index(request):
    doc_externo=open("C:\\Users\\d-sko\\Desktop\\pag\\PRUEBA\\index.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

def base(request):
    doc_externo=open("C:\\Users\\d-sko\\Desktop\\pag\\PRUEBA\\PRUEBA\\__base.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)
