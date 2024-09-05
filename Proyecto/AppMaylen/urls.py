from django.urls import path
from AppMaylen import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),

    path('crear-curso/', views.CursoCreateView.as_view(), name='create_curso'),
    path('cursos/', views.CursoListView.as_view(), name='lista_curso'),
    path('detalle-curso/<pk>', views.CursoDetailView.as_view(), name='detalle_curso'),
    path('curso/<pk>/editar', views.CursoUpdateView.as_view(), name='editar_curso'),
    path('curso/<pk>/borrar', views.CursoDeleteView.as_view(), name='borrar_curso'),

    path('crear-profesor/', views.ProfesorCreateView.as_view(), name='create_profesor'),
    path('profesores/', views.ProfesorListView.as_view(), name='lista_profesor'),
    path('detalle-profesor/<pk>', views.ProfesorDetailView.as_view(), name='detalle_profesor'),
    path('profesor/<pk>/editar', views.ProfesorUpdateView.as_view(), name='editar_profesor'),
    path('profesor/<pk>/borrar', views.ProfesorDeleteView.as_view(), name='borrar_profesor'),

    path('about/', views.AboutUsView.as_view(), name="about"),
    path('contact/', views.ContactUsView.as_view(), name="contact"),
]