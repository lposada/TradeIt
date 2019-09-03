from django.shortcuts import render
from django.http import HttpResponse
from .forms import UsuarioFormulario, UsuarioExistente

# Create your views here.
Usuarios = [
        {'Nombre': 'Luis', 'Id':'1040755645', 'Tipo':'C.C.', 'Email':'lposad25@eafit.edu.co'},
        {'Nombre': 'Jorge', 'Id':'3353095','Tipo':'C.C.','Email':'joiper255@gmail.com'},
        {'Nombre': 'Ines', 'Id':'43034468','Tipo':'C.C.','Email':'ines462@gmail.com'},
        {'Nombre': 'ASD', 'Id':'123456789','Tipo':'C.C.','Email':'asd@asd.com'}
]

def entrada(request):
        return render(request, 'inicio.html',)

def get_item(id):
        for usuario in Usuarios:
                if usuario['Id'] == id:
                        return "Nombre:" + usuario['Nombre'] + " Id:" + usuario['Id'] + " Tipo:" + usuario['Tipo'] + " Email:" + usuario['Email']
                else:
                        return "No Existe"

def existente(request):

        if request.method == 'POST':
                form = UsuarioExistente(request.POST)
                if form.is_valid():
                        ids = form.cleaned_data['Id']
                        print(get_item(ids))
        form = UsuarioExistente()
        return render(request, 'existente.html', {'form': form})


def contact(request):


    if request.method == 'POST':
        form = UsuarioFormulario(request.POST)
        if form.is_valid():

            name = form.cleaned_data['Nombre']
            email = form.cleaned_data['Email']
            tipo = form.cleaned_data['Tipo']
            ids = form.cleaned_data['Id']
            Usuarios.append({'Nombre': name, 'Id': ids, 'Tipo': tipo, 'Email': email})
    form = UsuarioFormulario()
    return render(request, 'form.html', {'form': form})
