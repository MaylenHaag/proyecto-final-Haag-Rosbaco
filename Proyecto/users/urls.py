from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views


urlpatterns = [
    path ('login/', views.login_request, name='Login'),
    path ('register/', views.register, name='Register'),
    path ('logout/', LogoutView.as_view(template_name="users/logout.html"), name="Logout"),

    path ('editar_usuario/', views.editar_usuario, name='EditarUsuario'),
    path ('cambiar_password', views.CambiarPasswordView.as_view(), name="CambiarPassword"),

    path('crear-estudiante/', views.EstudianteCreateView.as_view(), name='create_estudiante'),
    path('estudiantes/', views.EstudianteListView.as_view(), name='lista_estudiantes'),
    path('detalle-estudiante/<pk>', views.EstudianteDetailView.as_view(), name='detalle_estudiante'),
    path ('estudiante/<int:pk>', views.EstudianteDeleteView.as_view(), name='borrar_estudiante'),
    path ('estudiante/<int:pk>/actualizar', views.EstudianteUpdateView.as_view(), name='editar_estudiante'),
]