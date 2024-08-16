from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from AppMaylen.models import Estudiante


class EstudianteListView(ListView):
    model = Estudiante
    context_object_name = "Estudiantes"
    template_name = "vbc/lista_estudiantes.html"


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = "vbc/estudiante_borrar.html"
    success_url = reverse_lazy("EstudianteBorrar")


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    template_name = "vbc/actualiza_estudiante.html"
    success_url = reverse_lazy("ListarEstudiantes")
    fields = ["nombre", "apellido"]



