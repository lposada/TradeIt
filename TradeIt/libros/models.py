from django.db import models

# Create your models here.
class Libro(models.Model):
    title = models.CharField(max_length=80, verbose_name="Titulo")
    autor = models.CharField(max_length=80, verbose_name="Autor")
    tipo = models.CharField(max_length=80, verbose_name="Tipo")
    id = models.SmallIntegerField(primary_key=True, verbose_name="Identificador")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "libro"
        verbose_name_plural = "libros"
        ordering = ['-created']
    
    def __str__(self):
        return self.title
