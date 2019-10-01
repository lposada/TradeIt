from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from .forms import UsuariosForm, TruequesForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from .models import Usuario
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
# Create your views here.
personal = Group(name = "Personal")

def check_admin(user):
    return user.groups.filter(name='Personal').exists()

@user_passes_test(check_admin)
def usuarios(request):
    return render(request, 'usuarios/usuarios.html')

class ListUsuarios(ListView):
    model = Usuario

class DetailUsuario(DetailView):
    model = Usuario

class CrearUsuario(CreateView):
    model = Usuario
    form_class = UsuariosForm
    success_url = reverse_lazy('usuarios:usuarios')

class TruequesView(UpdateView):
    model = Usuario
    form_class = TruequesForm
    template_name = 'usuarios/usuario_trueque_form.html'
    def get_success_url(self):
        return reverse_lazy('usuarios:trueques', args=[self.object.id]) + '?ok'

class DeleteUsuario(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuarios:usuarios')

