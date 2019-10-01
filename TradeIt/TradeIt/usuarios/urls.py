from django.urls import path
from . import views as views
from .views import ListUsuarios, DetailUsuario, CrearUsuario, DeleteUsuario, TruequesView

usuarios_patterns = ([
    path('', ListUsuarios.as_view(), name="usuarios"),
    path('<int:pk>/<slug:slug>/', DetailUsuario.as_view(), name='usuario'),
    path('crear/', CrearUsuario.as_view(), name="crear"),
    path('delete/<int:pk>/', DeleteUsuario.as_view(), name='delete'),
    path('trueque/<int:pk>/', TruequesView.as_view(), name='trueques'),
], 'usuarios')