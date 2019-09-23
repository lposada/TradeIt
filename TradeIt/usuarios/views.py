from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse
from .forms import UsuariosForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from .models import Usuario

# Create your views here.
personal = Group(name = "Personal")

def check_admin(user):
    return user.groups.filter(name='Personal').exists()

@user_passes_test(check_admin)
def usuarios(request):
    return render(request, 'usuarios/usuarios.html')

def agregar(request):
    usuario_form = UsuariosForm()
    if request.method == "POST":
        usuario_form = UsuariosForm(data=request.POST)
        if usuario_form.is_valid():
            obj = Usuario()
            obj.name = usuario_form.cleaned_data['name']
            obj.email = usuario_form.cleaned_data['email']
            obj.id = usuario_form.cleaned_data['id']
            obj.tipo = usuario_form.cleaned_data['tipo']
            #Suponemos que todo ha ido bien redireccionamos
            obj.save()
            return redirect(reverse('agregar')+"?ok")

    return render(request, 'usuarios/agregar.html', {'form':usuario_form})

def existente(request):
    query = request.GET.get('q','')
    #The empty string handles an empty "request"
    if query:
            queryset = (Q(id__icontains=query))
            #I assume "text" is a field in your model
            #i.e., text = model.TextField()
            #Use | if searching multiple fields, i.e., 
            #queryset = (Q(text__icontains=query))|(Q(other__icontains=query))
            results = Usuario.objects.filter(queryset).distinct()
    else:
       results = []
    return render(request, 'usuarios/existente.html', {'results':results, 'query':query})       

def eliminar(request):
    return render(request, 'usuarios/eliminar.html')

