from django.contrib import admin
from .models import Libro
# Register your models here.
class LibrosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','autor', 'tipo')

admin.site.register(Libro, LibrosAdmin)