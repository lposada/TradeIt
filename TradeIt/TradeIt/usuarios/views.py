from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from .forms import UsuariosForm, UsuariosFormUpdate
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from .models import Usuario
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class ListUsuarios(ListView):
    model = Usuario
    paginate_by = 10
    def get_queryset(self): # new
        object_list = Usuario.objects.all()
        query = self.request.GET.get('buscar')
        if query:
            object_list = Usuario.objects.filter(
                Q(nombre__icontains=query) | Q(id__icontains=query) | Q(email__icontains=query)
            )

        return object_list

@method_decorator(staff_member_required, name='dispatch')
class DetailUsuario(DetailView):
    model = Usuario

@method_decorator(staff_member_required, name='dispatch')
class CrearUsuario(CreateView):
    model = Usuario
    form_class = UsuariosForm
    success_url = reverse_lazy('usuarios:usuarios')

@method_decorator(staff_member_required, name='dispatch')
class UpdateUsuario(UpdateView):
    model = Usuario
    form_class = UsuariosFormUpdate
    success_url = reverse_lazy('usuarios:usuarios')
    template_name = 'usuarios/usuario_form_update.html'

@method_decorator(staff_member_required, name='dispatch')
class DeleteUsuario(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuarios:usuarios')
