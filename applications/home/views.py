from applications.persona.models import Empleado
from django.shortcuts import render

from django.views.generic import(
    TemplateView,
    ListView,
    CreateView,
)
# Create your views here.
class InicioView(TemplateView):
    template_name = 'inicio.html'
#------------------------------------------------
class PruebaView(TemplateView):
    template_name = "home/prueba.html"

class PruebaView(TemplateView):
    template_name = "home/resumen_foundation.html"


class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['0','10','20','30']

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Empleado
    fields = ["first_name","last_name"]
    
    

