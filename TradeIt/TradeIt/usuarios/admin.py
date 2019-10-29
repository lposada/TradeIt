from django.contrib import admin
from .models import Usuario
# Register your models here.
class UsuariosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre','tipo', 'id')

admin.site.register(Usuario, UsuariosAdmin)