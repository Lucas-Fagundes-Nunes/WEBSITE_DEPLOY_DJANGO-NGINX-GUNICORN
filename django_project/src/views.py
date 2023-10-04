# myapp/views.py

from django.shortcuts import render

def home(request):
    context = {
        'mensagem': 'Olá, Seja bem-vindo a página de testes HOME!',
    }
    return render(request, 'home/index.html', context)

def teste(request):
    context = {
        'mensagem': 'BEM-VINDO!!',
    }
    return render(request, 'home/index.html', context)