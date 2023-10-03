# myapp/views.py

from django.shortcuts import render

def home(request):
    context = {
        'mensagem': 'Olá, esta é a minha página de exemplo!',
    }
    return render(request, 'home/index.html', context)

def teste(request):
    context = {
        'mensagem': 'Olá, esta é a minha página TESTE',
    }
    return render(request, 'home/index.html', context)