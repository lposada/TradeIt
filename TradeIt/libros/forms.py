from django import forms
from .choices import tipo
class LibrosForm(forms.Form):
    title = forms.CharField(label="Titulo", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe el titulo del libro.'}))
    autor = forms.CharField(label="Autor", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe el autor del libro.'}))
    tipo = forms.ChoiceField(choices=tipo,label="Tipo", required=True, widget=forms.Select(attrs={'class':'form-control'}))
    id = forms.IntegerField(label="Id", required=True, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Escribe el id del libro'}))