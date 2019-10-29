from django import forms
from .choices import direccionalidad
from .models import Trueque

class TruequesForm(forms.ModelForm):

    class Meta:
        model = Trueque
        fields = ['direccionalidad', 'usuario', 'libro']
        widgets = {
            'usuario' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese el numero de identificacion'}),
            'libro' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese el identificador del libro'}),
            'direccionalidad' : forms.Select(attrs={'class':'form-control'}, choices=direccionalidad),
        }
        

    