from django.db import models
from users.models import Usuario

# Create your models here.

class TipoServicio(models.Model):
    nombre = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.nombre
    
class Solicitud(models.Model):
    tipo = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    descripcion = models.CharField(max_length=500,blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.descripcion

class Agendamiento(models.Model):
    solicitud = models.OneToOneField(
        Solicitud,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    tipo = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    descripcion = models.CharField(max_length=500,blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    direccion = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.descripcion