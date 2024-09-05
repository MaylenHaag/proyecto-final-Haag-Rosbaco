from django.contrib import admin
from AppMaylen.models import Curso
from users.models import Estudiante

# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)