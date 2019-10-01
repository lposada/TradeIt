from django import forms
from .choices import tipo
from .models import Usuario
class UsuariosForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['name','tipo','id','email','trueques']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe tu Nombre.'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Escribe tu Correo.'}),
            'tipo' : forms.Select(attrs={'class':'form-control'}, choices=tipo),
            'id' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Escribe tu cedula'}),
            'trueques' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Numero de trueques'}),
        }

class TruequesForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['name','id','email','trueques']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'id' : forms.NumberInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'trueques' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Agregar trueques'}),
        }
    