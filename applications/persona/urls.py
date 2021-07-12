from django.urls import path
from . import views
app_name = "persona_app"
urlpatterns = [
    path('listar-todos-empleados/', views.ListAllEmpleados.as_view(), name='empleado_all'),
    path('lista-empleados-admin/', views.ListAllEmpleadosAdmin.as_view(), name='empleados_admin'),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('listar-by-area/<pk>/', views.ListByAreaEmpleado.as_view(), name='empleados_area'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name="modificar_empleado"),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name="eliminar_empleado"),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='empleado_add'),
    #-------------------------------------------------------------------------------------------------
    path('buscar-empleado/', views.ListEmpleadosByword.as_view()),
    path('listar-habilidades-empleado/', views.ListHabilidadesEmpleado.as_view()),
    
    path('success/', views.SuccessView.as_view(), name="correcto"),
]