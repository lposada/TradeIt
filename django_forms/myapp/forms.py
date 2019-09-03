from django import forms

class UsuarioFormulario(forms.Form):
    Nombre = forms.CharField()
    Email = forms.EmailField(label='E-Mail')
    Tipo = forms.ChoiceField(choices=[('c.c.','C.C.'),('t.i.','T.I.'),('pasaporte','Pasaporte')])
    Id = forms.CharField()

class UsuarioExistente(forms.Form):
    Id = forms.CharField()