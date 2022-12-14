from multiprocessing import context
from urllib import request
from django.shortcuts import render
from principal.models import *

def index(request):
    return render(request, 'index.html')

def relogios(request):
    lista = Relogio.objects.all()
    context = {'relogios' : lista }
    return render(request, 'relogios.html', context)

def expandido(request, id):
    relogio = Relogio.objects.get(id=id)
    context = {'relogio' : relogio}
    return render(request, 'expandido.html', context)

def quemsomos(request):
    return render(request, 'quemsomos.html')