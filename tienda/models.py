from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) :
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self) :
        return self.nombre

class Cliente(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    direccion =models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    fch_nac = models.DateField('Fecha de nacimiento')
    pub_date = models.DateTimeField('date published')
    def __str__(self) :
        return self.nombres