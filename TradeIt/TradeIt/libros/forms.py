from django import forms
from .choices import tipo
from .models import Libro
class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['title','autor','tipo']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo.'}),
            'autor' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Autor.'}),
            'tipo' : forms.Select(attrs={'class':'form-control'}, choices=tipo),
        }
    