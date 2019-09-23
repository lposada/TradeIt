from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LibrosForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from .models import Libro
# Create your views here.
personal = Group(name = "Personal")

def check_admin(user):
    return user.groups.filter(name='Personal').exists()

@user_passes_test(check_admin)
def libros(request):
    libro_form = LibrosForm()
    if request.method == "POST":
        libro_form = LibrosForm(data=request.POST)
        if libro_form.is_valid():
            obj = Libro()
            obj.title = libro_form.cleaned_data['title']
            obj.autor = libro_form.cleaned_data['autor']
            obj.id = libro_form.cleaned_data['id']
            obj.tipo = libro_form.cleaned_data['tipo']
            #Suponemos que todo ha ido bien redireccionamos
            obj.save()
            return redirect(reverse('libros')+"?ok")

    return render(request, 'libros/libros.html', {'form':libro_form})
