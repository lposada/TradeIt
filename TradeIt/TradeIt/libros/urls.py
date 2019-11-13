from django.urls import path
from . import views as views
from .views import ListLibro, DetailLibro, CrearLibro, DeleteLibro, UpdateLibro, DetailLibroQR, EscanearQR

libros_patterns = ([
    path('', ListLibro.as_view(), name='libros'),
    path('<int:pk>/', DetailLibro.as_view(), name='libro'),
    path('/', DetailLibroQR.as_view(), name='libroQR'),
    path('crear/', CrearLibro.as_view(), name='crearlibro'),
    path('delete/<int:pk>/', DeleteLibro.as_view(), name='delete'),
    path('update/<int:pk>/', UpdateLibro.as_view(), name='update'),
    path('escanear/', EscanearQR, name="escanear"),
], 'libros')