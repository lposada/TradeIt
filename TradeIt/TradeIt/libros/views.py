from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .forms import LibroForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from .models import Libro
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class ListLibro(ListView):
    model = Libro
    paginate_by = 10
    def get_queryset(self): # new
        object_list = Libro.objects.all()
        query = self.request.GET.get('buscar')
        if query:
            object_list = Libro.objects.filter(
                Q(title__icontains=query) | Q(autor__icontains=query) | Q(tipo__icontains=query) | Q(id__icontains=query) | Q(editorial__icontains=query)
            )

        return object_list
        
@method_decorator(staff_member_required, name='dispatch')
class DetailLibro(DetailView):
    model = Libro

@method_decorator(staff_member_required, name='dispatch')
class DetailLibroQR(DetailView):
    model = Libro

    def get_object(self):
        return Libro.objects.get(pk=self.request.GET.get('id_libro'))

@method_decorator(staff_member_required, name='dispatch')
class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    def get_success_url(self):
        return reverse_lazy('libros:libros') + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class UpdateLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/libro_form_update.html'
    success_url = reverse_lazy('libros:libros')

@method_decorator(staff_member_required, name='dispatch')
class DeleteLibro(DeleteView):
    model = Libro
    success_url = reverse_lazy('libros:libros')


def EscanearQR(request):
    model = Libro
    form_class = LibroForm
    return render(request, "libros/escanear_qr.html")

