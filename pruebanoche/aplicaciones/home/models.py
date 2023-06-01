from django.db import models

# Create your models here.

class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100)
    año = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

def __str__(self):
    return self.titulo+''+self.subtitulo+''+self.cantidad+''+self.año+''+self.tipo