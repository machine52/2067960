from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre            = models.CharField(max_length = 100) 
    descripcion       = models.TextField(max_length = 500)

    def __str__ (self):
        return self.nombre

class Marca (models.Model):
    nombre           = models.CharField(max_length = 100)

    def __str__ (self):
        return self.nombre

class producto (models.Model):
    nombre      = models.CharField(max_length = 100)
    descripcion = models.TextField(max_length = 500)
    precio      = models.IntegerField()
    cantidad    = models.IntegerField()
    activo      = models.BooleanField(default = True)
    foto        = models.ImageField(upload_to = 'productos', null=True, blank=True)
    marca       = models.ForeignKey(Marca, models.PROTECT)
    categoria   = models.ManyToManyField(Categoria, null=True, blank=True)

    def __str__(self):
        return self.nombre  + str(self.precio)      
