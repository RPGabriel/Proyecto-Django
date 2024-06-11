from django.db import models

# Create your models here.
class Alumnos(models.Model):
    matricula = models.CharField(max_length=12) #Define la estructura de nuestra tabla
    nombre = models.TextField() #texto corto
    carrera = models.TextField() #texto largo
    turno = models.CharField(max_length=10)
    created =models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now_add=True)
