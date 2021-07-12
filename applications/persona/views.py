from applications.departamento.models import Departamento
from django.shortcuts import render
from django.urls import reverse_lazy
from applications.persona.models import Empleado
from applications.persona.forms import EmpleadoForm
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
# Create your views here.

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    #model = Empleado
    paginate_by = 3
    ordering = 'first_name'
    #context_object_name = "lista"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword","")
        lista = Empleado.objects.filter(
            first_name__icontains = palabra_clave
        )
        return lista

class ListAllEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleado.html'
    #model = Empleado
    paginate_by = 3
    ordering = 'first_name'
    context_object_name = "empleados"
    model = Empleado

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Ejemplo de titulo'
        return context

class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    #queryset = Empleado.objects.filter(
    #    departamento__name = "Contabilidad"
    #)

    def get_queryset(self):
        id = self.kwargs["pk"]
        lista = Empleado.objects.filter(
            departamento__pk = id
        )
        return lista
    
    def get_context_data(self, **kwargs):
        context = super(ListByAreaEmpleado, self).get_context_data(**kwargs)
        id = self.kwargs["pk"]
        depa = Departamento.objects.get(pk=id)
        context['area'] = depa.name
        return context

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        "first_name",
        "last_name",
        "job",
        "departamento",
        "habilidades",
    ]
    success_url = reverse_lazy("persona_app:empleados_admin")

    ##PRIMERO
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST["last_name"])
        return super().post(request, *args, **kwargs)

    ##SEGUNDO
    def form_valid(self, form):
        print("METODO FORM VALID")
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy("persona_app:empleados_admin")

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    """
    fields = [
        "first_name",
        "last_name",
        "job",
        "departamento",
        "habilidades",
        "avatar"
    ]
    """
    #fields = ('__all__')
    success_url = reverse_lazy("persona_app:empleado_all")

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name+ " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
#------------------------------------------------------------------------------------------
class ListEmpleadosByword(ListView):
    template_name = "persona/by_kword.html"
    context_object_name = "empleados"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword","")
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista
    
class ListHabilidadesEmpleado(ListView):

    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=3)
        return empleado.habilidades.all()
    
class SuccessView(TemplateView):
    template_name = "persona/success.html"



