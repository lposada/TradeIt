from django import forms
from .choices import tipo
from .models import Usuario


class UsuariosForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'tipo','id','email','eafit','fecha_nacimiento','tyc']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el Nombre.'}),
            'apellido' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el Apellido'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Escriba el Correo.'}),
            'tipo' : forms.Select(attrs={'class':'form-control'}, choices=tipo),
            'id' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Escriba el numero de identificacion'}),
            'eafit' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'tyc' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'fecha_nacimiento' : forms.SelectDateWidget(years=range(1920, 2013), attrs={'style': 'width: 33%; display: inline-block;'}),
        }

class UsuariosFormUpdate(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'tipo','id','email','eafit','fecha_nacimiento','tyc']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el Nombre.'}),
            'apellido' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el Apellido'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Escriba el Correo.'}),
            'tipo' : forms.Select(attrs={'class':'form-control'}, choices=tipo),
            'id' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Escriba el numero de identificacion', 'disabled':'true'}),
            'eafit' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'tyc' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'fecha_nacimiento' : forms.SelectDateWidget(years=range(1920, 2013), attrs={'style': 'width: 33%; display: inline-block;'}),
        }
    