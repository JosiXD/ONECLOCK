from multiprocessing import context
from urllib import request
from django.shortcuts import render
from principal.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

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

def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            print("Enviado com sucesso")
            form = ContatoForm()
        else:
            print("Erro ao enviar email")
    context = {'form': form}

    return render(request, 'contato.html', context)

@login_required
def administracao(request):
    return render(request, 'administracao.html')

def logout_aplicacao(request):
    logout(request)
    return redirect('login')