from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=80, verbose_name="Nombre")
    email = models.EmailField(max_length=80, verbose_name="Correo")
    tipo = models.CharField(max_length=80, verbose_name="Tipo")
    id = models.IntegerField(primary_key=True, verbose_name="Identificador", default=0)
    trueques = models.SmallIntegerField(verbose_name="Trueques")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        ordering = ['-created']
    
    def __str__(self):
        return self.name