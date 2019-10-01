from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .forms import LibroForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from .models import Libro
# Create your views here.

class ListLibro(ListView):
    model = Libro

class DetailLibro(DetailView):
    model = Libro

class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    def get_success_url(self):
        return reverse_lazy('libros:crearlibro') + '?ok'


class DeleteLibro(DeleteView):
    model = Libro
    success_url = reverse_lazy('libros:libros')

