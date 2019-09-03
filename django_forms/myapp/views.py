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
                        user = usuario
                        break
                else:
                        user = "No Existe"
        return user

def existente(request):
        usuario = "Introduzca el id del usuario"
        if request.method == 'POST':
                form = UsuarioExistente(request.POST)
                if form.is_valid():
                        ids = form.cleaned_data['Id']
                        usuario = get_item(ids)
                        nombre = usuario['Nombre']
                        cedula = usuario['Id']
                        tipo = usuario['Tipo']
                        correo = usuario['Email']
        form = UsuarioExistente()

        return render(request, 'existente.html', {'form': form, 'nombre': "Nombre: " + nombre, 'tipo': "Tipo: " + tipo, 'cedula': "Id: " + cedula, 'correo': "Correo: " + correo,})


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
