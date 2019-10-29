from django.contrib import admin
from .models import Trueque

# Register your models here.
class TruequeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id','direccionalidad', 'usuario', 'libro')

admin.site.register(Trueque, TruequeAdmin)