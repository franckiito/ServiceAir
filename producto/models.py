from django.db import models

# Create your models here.

class Bodega(models.Model):
    nombre = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=500,blank=True)
    direccion = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.nombre

class TipoFuncionamiento(models.Model):
    nombre = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoFuncionamiento, on_delete=models.CASCADE)

    sku = models.CharField(max_length=50, blank=True)
    nombre = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=500,blank=True)
    modelo = models.CharField(max_length=50,blank=True)
    capacidad = models.IntegerField(blank=True)
    cadal models.CharField(max_length=50,blank=True)
    voltaje = models.IntegerField(blank=True)
    consumo = models.IntegerField(blank=True)
    corriente = models.IntegerField(blank=True)
    nivel_sonoro = models.CharField(max_length=50,blank=True)
    dimensiones models.CharField(max_length=50,blank=True)
    peso = models.IntegerField(blank=True)
    refrigerante = models.CharField(max_length=50,blank=True)

    estado = models.IntegerField(blank=True)

    def __str__(self):
        return self.nombre
    
class TipoRepuesto(models.Model):
    nombre = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.nombre

class Repuesto(models.Model):
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoRepuesto, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.nombre