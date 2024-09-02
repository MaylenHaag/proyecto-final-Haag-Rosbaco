from django.urls import path
from AppMaylen import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear-curso/', views.CursoCreateView.as_view(), name='create_curso'),
    path('cursos/', views.CursoListView.as_view(), name='curso_list'),
    path('crear-estudiante/', views.EstudianteCreateView.as_view(), name='create_estudiante'),
    path('estudiantes/', views.EstudianteListView.as_view(), name='estudiante_list'),
    path('crear-profesor/', views.ProfesorCreateView.as_view(), name='create_profesor'),
    path('profesores/', views.ProfesorListView.as_view(), name='profesor_list'),
    path('crear-entregable/', views.EntregableCreateView.as_view(), name='create_entregable'),
    path('entregables/', views.EntregableListView.as_view(), name='entregable_list'),
    path('about/', views.AboutUsView.as_view(), name="about")
]