from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Curso, Estudiante, Profesor, Entregable
from .forms import CursoForm, EstudianteForm, ProfesorForm, EntregableForm

# Vista para la página principal con formularios y listas
def index(request):
    if request.method == 'POST':
        if 'curso_submit' in request.POST:
            form = CursoForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'estudiante_submit' in request.POST:
            form = EstudianteForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'profesor_submit' in request.POST:
            form = ProfesorForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'entregable_submit' in request.POST:
            form = EntregableForm(request.POST)
            if form.is_valid():
                form.save()

    cursos = Curso.objects.all()
    estudiantes = Estudiante.objects.all()
    profesores = Profesor.objects.all()
    entregables = Entregable.objects.all()

    return render(request, 'AppMaylen/index.html', {
        'curso_form': CursoForm(),
        'estudiante_form': EstudianteForm(),
        'profesor_form': ProfesorForm(),
        'entregable_form': EntregableForm(),
        'cursos': cursos,
        'estudiantes': estudiantes,
        'profesores': profesores,
        'entregables': entregables,
    })

def about(request) :
    return render(request, "AppMaylen/about.html")

# Vista para crear un curso
class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'AppMaylen/create_curso.html'
    success_url = reverse_lazy('curso_list')

# Vista para listar cursos
class CursoListView(ListView):
    model = Curso
    template_name = "AppMaylen/curso_list.html"
    context_object_name = 'cursos'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print("Usuario autenticado:", request.user)
        else:
            print("Usuario no autenticado")
        return super().get(request, *args, **kwargs)


# Vista para crear un estudiante
class EstudianteCreateView(LoginRequiredMixin, CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'AppMaylen/create_estudiante.html'
    success_url = reverse_lazy('estudiante_list')

# Vista para listar estudiantes
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'AppMaylen/estudiante_list.html'
    context_object_name = 'estudiantes'

# Vista para crear un profesor
class ProfesorCreateView(LoginRequiredMixin, CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'AppMaylen/create_profesor.html'
    success_url = reverse_lazy('profesor_list')

# Vista para listar profesores
class ProfesorListView(ListView):
    model = Profesor
    template_name = 'AppMaylen/profesor_list.html'
    context_object_name = 'profesores'

# Vista para crear un entregable
class EntregableCreateView(LoginRequiredMixin, CreateView):
    model = Entregable
    form_class = EntregableForm
    template_name = 'AppMaylen/create_entregable.html'
    success_url = reverse_lazy('entregable_list')

# Vista para listar entregables
class EntregableListView(ListView):
    model = Entregable
    template_name = 'AppMaylen/entregable_list.html'
    context_object_name = 'entregables'


class AboutUsView(TemplateView):
    template_name = "AppMaylen/about.html"