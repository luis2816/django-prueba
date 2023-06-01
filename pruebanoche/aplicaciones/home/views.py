from django.urls import reverse_lazy

from django.shortcuts import render
# Create your views here.
from.models import Prueba

from django.views.generic import TemplateView, CreateView, DeleteView, ListView, UpdateView

from .forms import PruebaForm

class PruebaView(TemplateView):
    template_name="prueba.html"


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "crear.html"
    form_class = PruebaForm
    success_url= '/crear'

    def get_success_url(self):
        # Personaliza la URL de redirección después de la eliminación
        return reverse_lazy('lista')

class PruebaListView(ListView):
    model = Prueba
    template_name = "listar.html"
    context_object_name = 'prueba'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actualizar_url'] = reverse_lazy('actualizar', kwargs={'pk': 0})  # Valor de ejemplo para evitar error de variable indefinida
        return context

class PruebaUpdateView(UpdateView):
    model = Prueba
    fields = ['titulo', 'subtitulo', 'cantidad', 'año', 'tipo']  # Lista de campos que deseas editar
    template_name = "actualizar.html"

    def get_success_url(self):
        # Personaliza la URL de redirección después de la actualización
        return reverse_lazy('lista')


class PruebaDeleteView(DeleteView):
    model = Prueba
    template_name = "eliminar.html"

    def get_success_url(self):
        # Personaliza la URL de redirección después de la eliminación
        return reverse_lazy('lista')






