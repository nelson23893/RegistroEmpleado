# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categoria(models.Model):

    nombre  =   models.CharField(max_length=30)


    def __str__(self):

        return self.nombre

class Empleado(models.Model):
    nombre    = models.CharField(max_length=60)

    edad      = models.IntegerField()

    categorias   = models.ManyToManyField(Categoria, through='Puesto')

    def __str__(self):

        return self.nombre


 class Puesto (models.Model):

    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)


class PuestoInLine(admin.TabularInline):

    model = Puesto

#muestra una linea extra al momento de insertar, como indicación al usuario que se pueden ingresar varios actores.

    extra = 1


class CategoriaAdmin(admin.ModelAdmin):

    inlines = (ActuacionInLine,)


class EmpleadoAdmin (admin.ModelAdmin):

    inlines = (ActuacionInLine,)