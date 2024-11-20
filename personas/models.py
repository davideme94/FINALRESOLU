# personas/models.py

from django.db import models

class Persona(models.Model):
    dni = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Documento(models.Model):
    persona = models.ManyToManyField(Persona, related_name='documentos')
    descripcion = models.TextField()
    pdf_url = models.URLField()

    def __str__(self):
        return self.descripcion
