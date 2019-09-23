from django.urls import path
from . import views as views

urlpatterns = [
    path('', views.usuarios, name="usuarios"),
    path('agregar/', views.agregar, name="agregar"),
    path('existente/', views.existente, name="existente"),
    path('eliminar/', views.eliminar, name="eliminar"),
]