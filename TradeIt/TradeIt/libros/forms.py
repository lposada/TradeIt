from django import forms
from .choices import tipo
from .models import Libro
class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['id','title','autor','tipo','editorial']
        widgets = {
            'id' : forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'id'}),
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo.'}),
            'autor' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Autor.'}),
            'tipo' : forms.Select(attrs={'class':'form-control'}, choices=tipo),
            'editorial' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Editorial'}),
        }
    