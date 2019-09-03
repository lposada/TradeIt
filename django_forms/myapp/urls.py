from django.urls import path
from . import views

urlpatterns = [
    path('', views.entrada),
    path('crearcontacto', views.contact),
    path('usuarioexistente', views.existente),
]