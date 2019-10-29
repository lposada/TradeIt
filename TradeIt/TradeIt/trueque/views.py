from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .forms import TruequesForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from .models import Trueque
from .forms import TruequesForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class ListTrueque(ListView):
    model = Trueque

@method_decorator(staff_member_required, name='dispatch')
class CrearTrueque(CreateView):
    model = Trueque
    form_class = TruequesForm
    success_url = reverse_lazy('trueque:trueques')

    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial['libro'] = self.request.GET[x]
        print(initial)
        return initial

@method_decorator(staff_member_required, name='dispatch')
def EscanearQR (request):
    model = Trueque
    form_class = TruequesForm
    return render(request, "trueque/escanear_qr.html")