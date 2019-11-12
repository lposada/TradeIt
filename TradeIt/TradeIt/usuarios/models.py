from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre", blank=False)
    apellido = models.CharField(max_length=30, verbose_name="Apellido", blank=False)
    email = models.EmailField(max_length=80, verbose_name="Correo", blank=False)
    tipo = models.CharField(max_length=80, verbose_name="Tipo", blank=False)
    id = models.BigIntegerField(primary_key=True, verbose_name="Identificador", blank=False)
    saldo = models.SmallIntegerField(verbose_name="Saldo", default=0)
    eafit = models.BooleanField(verbose_name="Miembro EAFIT", default=False)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento", blank=False)
    tyc = models.BooleanField(verbose_name="Terminos y Condiciones", default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        ordering = ['-created']
    
    def __str__(self):
        return str(self.id)