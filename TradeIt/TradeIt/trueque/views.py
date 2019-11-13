from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, TemplateView
from .forms import TruequesForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from .models import Trueque
from .forms import TruequesForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from libros.models import Libro
from usuarios.models import Usuario
from django.views.generic import View
from django.utils import timezone
from .render import Render
from django.db import InternalError
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class ListTrueque(ListView):
    model = Trueque
    paginate_by = 10

@method_decorator(staff_member_required, name='dispatch')
class CrearTrueque(CreateView):
    model = Trueque
    form_class = TruequesForm
    success_url = reverse_lazy('trueque:trueques')
    
    def form_valid(self, form):
        try:
            return super(CrearTrueque, self).form_valid(form)
        except InternalError as e:
            mensaje = format(e).split("CONTEXT")[0]
            return render(self.request, 'trueque/trueque_form.html', {'form': TruequesForm, 'messages': str(mensaje)})

    def form_invalid(self, form):
        if self.request.method == "POST":
            try:
                libro = form["libro"].value()
                us = form["usuario"].value()
                dirr = form["direccionalidad"].value()
                usuario = Usuario.objects.get(id=us)
                try:
                    obj = Libro.objects.create(id=libro)
                    try:              
                        trueque = Trueque.objects.create(libro=obj, usuario=usuario, direccionalidad=dirr)
                        return HttpResponseRedirect('/trueque/')
                    except:
                        None
                except:
                    obj = None
            except:
                None

        return super(CrearTrueque, self).form_invalid(form)
        

    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial['libro'] = self.request.GET[x]
        return initial

@method_decorator(staff_member_required, name='dispatch')
class GenerarReportes(TemplateView):
    template_name = "trueque/generar_reportes.html"

@method_decorator(staff_member_required, name='dispatch')
class Estadisticas(TemplateView):
    template_name = "trueque/estadisticas.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Estadisticas, self).get_context_data(*args, **kwargs)
        query_tipo = self.request.GET.get('tipo')
        object_list = None
        object_list2 = None
        query_fecha_inicial = self.request.GET.get('fechainicial')
        query_fecha_final = self.request.GET.get('fechafinal')
        query_editorial = self.request.GET.get('editorial')
        if query_fecha_final and query_fecha_inicial and (query_tipo=="contareditoriales"):
            object_list = Trueque.objects.order_by('libro__editorial').values('libro__editorial').distinct().filter(Q(created__range=(query_fecha_inicial, query_fecha_final))).count()

            context['object_list'] = str(object_list)
            context['mensaje'] = "Numero de editoriales participantes, entre las fechas {0} y {1}: ".format(query_fecha_inicial, query_fecha_final)
        
        if (query_tipo=="librosxeditorial") and query_editorial:
            object_list = Trueque.objects.distinct().filter(Q(libro__editorial=query_editorial)).count()

            context['object_list'] = str(object_list)
            context['mensaje'] = "Libros aportados por la editorial {0}: ".format(query_editorial)

        if (query_tipo=="cantidadtrueques") and query_fecha_final and query_fecha_inicial:
            entra = Trueque.objects.filter(Q(direccionalidad="Entra") & Q(created__range=(query_fecha_inicial, query_fecha_final))).count()
            sale = Trueque.objects.filter(Q(direccionalidad="Sale") & Q(created__range=(query_fecha_inicial, query_fecha_final))).count()
            object_list = sale
            object_list2 = entra-sale

            context['object_list'] = ""
            context['mensaje'] = "Cantidad de trueques totales entre las fechas {0} y {1}, Efectivos: {2} - Pendientes: {3}.".format(query_fecha_inicial, query_fecha_final, object_list, object_list2)
        if (query_tipo=="truequesxliterario") and query_fecha_final and query_fecha_inicial:
            novela = Trueque.objects.filter(Q(libro__tipo="Novela") & Q(created__range=(query_fecha_inicial, query_fecha_final))).count()
            poesia = Trueque.objects.filter(Q(libro__tipo="Poesia") & Q(created__range=(query_fecha_inicial, query_fecha_final))).count()
            ensayo = Trueque.objects.filter(Q(libro__tipo="Ensayo") & Q(created__range=(query_fecha_inicial, query_fecha_final))).count()
            cuento = Trueque.objects.filter(Q(libro__tipo="Cuento") & Q(created__range=(query_fecha_inicial, query_fecha_final))).count()
            otro = Trueque.objects.filter(Q(libro__tipo="Otro") & Q(created__range=(query_fecha_inicial, query_fecha_final))).count()
            mensaje = """Cantidad de trueques hechos por Genero Literario en las fechas {0} y {1}.
                                    Novela: {2}
                                    Poesia: {3}
                                    Ensayo: {4}
                                    Cuento: {5}
                                    Otro:   {6}""".format(query_fecha_inicial, query_fecha_final, novela, poesia, ensayo, cuento, otro)

            context['object_list'] = ""
            context['mensaje'] = mensaje
    
        return context
    
    

def EscanearQR (request):
    model = Trueque
    form_class = TruequesForm
    return render(request, "trueque/escanear_qr.html")


class Pdf(View):

    def get(self, request):
        trueques = Trueque.objects.all()
        query = self.request.GET.get('editorial')
        if query:
            trueques = Trueque.objects.filter(libro__editorial__contains=query, direccionalidad__contains='Sale')
            if query == "todas" or query == "Todas":
                trueques = Trueque.objects.all()
        hoy = timezone.now()
        params = {
            'hoy': hoy,
            'trueques': trueques,
            'request': request,
            'query' : query,
        }
        return Render.render('trueque/pdf.html', params)
