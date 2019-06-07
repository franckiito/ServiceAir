# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=500,blank=True)

class Usuario(AbstractUser):
    tipo = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    rut = models.CharField(max_length=11,blank=True)
    fecha_nac = models.DateField(auto_now_add=True)
    direccion = models.CharField(max_length=70,blank=True)
    telefono = models.CharField(max_length=12,blank=True)

    def __str__(self):
        return self.username
        
