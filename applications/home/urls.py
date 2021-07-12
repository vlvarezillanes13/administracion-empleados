from django.urls import path
from . import views


urlpatterns = [

    path('', views.InicioView.as_view(), name='inicio'),
    #--------------------------------------------------------------
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('crear/', views.PruebaCreateView.as_view()),
    path('resumen-foundation/', views.PruebaView.as_view()),
]