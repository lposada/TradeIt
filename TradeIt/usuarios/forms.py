from django import forms
from .choices import tipo
class UsuariosForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe tu Nombre.'}))
    email = forms.EmailField(label="Correo", required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Escribe tu Correo.'}))
    tipo = forms.ChoiceField(choices=tipo,label="Tipo", required=True, widget=forms.Select(attrs={'class':'form-control'}))
    id = forms.IntegerField(label="Cedula", required=True, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Escribe tu cedula'}))