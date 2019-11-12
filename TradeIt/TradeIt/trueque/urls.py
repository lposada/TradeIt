from django.urls import path
from . import views as views
from .views import CrearTrueque, ListTrueque, EscanearQR, Pdf, GenerarReportes, Estadisticas

trueque_patterns = ([
    path('', ListTrueque.as_view(), name="trueques"),
    path('crear', CrearTrueque.as_view(), name="crear"),
    path('escanear/', EscanearQR, name="escanear"),
    path('render/pdf/', Pdf.as_view(), name="reporte"),
    path('reportes/', GenerarReportes.as_view(), name="reportes"),
    path('estadisticas/', Estadisticas.as_view(), name="estadisticas"),
], 'trueque')