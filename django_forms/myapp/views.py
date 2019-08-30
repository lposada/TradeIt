from django.shortcuts import render
from django.http import HttpResponse
from .forms import UsuarioFormulario, UsuarioExistente

# Create your views here.
Nombre = 'asd'
Tipo = 'd'

def entrada(request):
        return render(request, 'inicio.html',)

def existente(request):
        if request.method == 'POST':
                form = UsuarioExistente(request.POST)
                if form.is_valid():
                        ids = form.cleaned_data['Id']
                        print(Nombre, Tipo)

        form = UsuarioExistente()
        return render(request, 'form.html', {'form': form})


def contact(request):


    if request.method == 'POST':
        form = UsuarioFormulario(request.POST)
        if form.is_valid():

            name = form.cleaned_data['Nombre']
            email = form.cleaned_data['Email']
            tipo = form.cleaned_data['Tipo']
            ids = form.cleaned_data['Id']
            global Nombre
            global Tipo
            Nombre = name
            Tipo = tipo
            print(name, email, tipo, ids)
    form = UsuarioFormulario()
    return render(request, 'form.html', {'form': form})