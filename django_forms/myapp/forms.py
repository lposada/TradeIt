from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

class UsuarioFormulario(forms.Form):
    Nombre = forms.CharField()
    Email = forms.EmailField(label='E-Mail')
    Tipo = forms.ChoiceField(choices=[('c.c.','C.C.'),('t.i.','T.I.'),('pasaporte','Pasaporte')])
    Id = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            'Nombre',
            'Email',
            'Tipo',
            'Id',
            Submit('submit', 'Crear', css_class='btn-sucess')
        )

class UsuarioExistente(forms.Form):
    Id = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            'Id',
            Submit('submit', 'Consultar', css_class='btn-sucess')
        )