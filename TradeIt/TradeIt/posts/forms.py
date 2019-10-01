from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','content','image','categories']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe el Titulo.'}),
            'content' : forms.Textarea(attrs={'class':'form-control'}),
            'image' : forms.ClearableFileInput(attrs=({'class':'form-control-file mt-3'})),
            #'categories' : forms.Select(choices= Category.objects.all()),
        }