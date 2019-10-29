from django.urls import path
from . import views as views
from .views import CrearTrueque, ListTrueque, EscanearQR

trueque_patterns = ([
    path('', ListTrueque.as_view(), name="trueques"),
    path('crear', CrearTrueque.as_view(), name="crear"),
    path('escanear/', EscanearQR, name="escanear"),
], 'trueque')