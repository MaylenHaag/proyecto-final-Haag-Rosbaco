from django.contrib import admin
from django.urls import path
from vbc import views

urlpatterns = [ 
    path ('estudiante/listar', views.EstudianteListView.as_view(), name='ListarEstudiantes'),
    path ('estudiante/<int:id>', views.EstudianteDeleteView.as_view(), name='EstudianteBorrar'),
    path ('estudiante/<int:id>/actualizar', views.EstudianteUpdateView.as_view(), name='ActualizarEstudiantes'),
    
] 