from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from AppMaylen.forms import EstudianteForm

from .models import Estudiante

from users.forms import UserRegisterForm, UserEditForm
from users.models import Avatar



# Vista para crear un estudiante
class EstudianteCreateView(LoginRequiredMixin, CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'AppMaylen/create_estudiante.html'
    success_url = reverse_lazy('lista_estudiantes')

# Vista para listar estudiantes
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'AppMaylen/lista_estudiantes.html'
    context_object_name = 'estudiantes'


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = "AppMaylen/borrar_estudiante.html"
    success_url = reverse_lazy("lista_estudiantes")


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    template_name = "AppMaylen/editar_estudiante.html"
    success_url = reverse_lazy("lista_estudiantes")
    fields = ["nombre", "apellido"]

class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = "AppMaylen/detalle_estudiante.html"


def login_request(request) :

    msg_login = ''

    if request.method == 'POST' :

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid() :

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None :
                login(request, user)
                return render(request, "AppMaylen/index.html")
            
        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})


def register(request) :
    
    msg_register = ''

    if request.method == 'POST' :

        form = UserRegisterForm(request.POST)

        if form.is_valid() :
            form.save()
            return render(request, "AppMaylen/index.html")
        
        else :
            msg_register = form.errors

    form = UserRegisterForm()
    return render(request, "users/registro.html", {"form": form, "msg_register": msg_register})    


@login_required
def editar_usuario(request) :

    usuario = request.user

    if request.method == 'POST' :
        formulario = UserEditForm(request.POST, request.FILES, instance = usuario) 
        
        if formulario.is_valid() :

            if formulario.cleaned_data.get("imagen") :
                avatar = Avatar(user=usuario, imagen=formulario.cleaned_data.get("imagen"))

                #usuario.avatar.imagen = formulario.cleaned_data.get("imagen")
                avatar.save()

            formulario.save()
            return render(request, "AppMaylen/index.html")
    else :
        formulario = UserEditForm(instance = usuario) 

    return render(request, "users/editar_usuario.html", {"form": formulario })   


class CambiarPasswordView(LoginRequiredMixin, PasswordChangeView) :
    tamplate_name = "users/cambiar_password.html"
    success_url = reverse_lazy("EditarUsuario")
    

class UserLogoutView(LogoutView):
    template_name = "users/logout.html"
    next_page = reverse_lazy("AppMaylen/index.html")
