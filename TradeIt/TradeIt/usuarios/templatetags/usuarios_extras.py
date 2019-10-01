from django import template
from usuarios.models import Usuario

register = template.Library()

@register.simple_tag
def get_usuario_list():
    usuarios = Usuario.objects.all()
    return usuarios