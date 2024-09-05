from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name="avatar")
    imagen = models.ImageField(upload_to="avatares", blank=True, null=True)

    def __str__(self) :
        return f"{self.user} - {self.imagen}"
    
    

class Estudiante (models.Model) :
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

    class Meta:
        db_table = 'users_estudiante'
