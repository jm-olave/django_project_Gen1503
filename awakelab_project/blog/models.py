from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default = timezone.now)
    autor = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.titulo
    def get_absolute_url(self):
        return reverse('publicacion-detalle', kwargs = {'pk': self.pk} )


class Reclamo(models.Model):
    nombre = models.CharField(max_length=100)
    cuerpo = models.TextField()

    def __str__(self):
        return self.nombre



