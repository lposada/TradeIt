from django.urls import path
from . import views as views
from .views import ListLibro, DetailLibro, CrearLibro, DeleteLibro

libros_patterns = ([
    path('', ListLibro.as_view(), name='libros'),
    path('<int:pk>/<slug:slug>/', DetailLibro.as_view(), name='libro'),
    path('crear/', CrearLibro.as_view(), name='crearlibro'),
    path('delete/<int:pk>/', DeleteLibro.as_view(), name='deletelibro'),
], 'libros')