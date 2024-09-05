from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Curso (models.Model) :
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    horario = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to='curso_imagenes/', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return "{} | ID: {}".format(self.nombre, self.id)


class Profesor (models.Model) :
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    imagen = models.ImageField(upload_to='profesor_imagenes/', null=True, blank=True)


class Entregable (models.Model) :
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()



    