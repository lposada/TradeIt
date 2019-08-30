from django.urls import path
from . import views

urlpatterns = [
    path('', views.entrada),
    path('usuarioexistente', views.existente),
    path('crearcontacto', views.contact),
]
