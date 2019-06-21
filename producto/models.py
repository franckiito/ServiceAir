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
    precio = models.IntegerField(blank=True)
    stock = models.IntegerField(blank=True)
    imagen = models.ImageField(upload_to='productos/')

    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.sku
    
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
    stock = models.IntegerField(blank=True)
    imagen = models.ImageField(upload_to='repuestos/')

    def __str__(self):
        return self.nombre
