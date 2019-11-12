from django.db import models
from usuarios.models import Usuario
from libros.models import Libro

# Create your models here.
class Trueque(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    direccionalidad = models.CharField(max_length=80, verbose_name="direccionalidad")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "trueque"
        verbose_name_plural = "trueque"
        ordering = ['-created']

    def __str__(self):
       return str(self.id)

