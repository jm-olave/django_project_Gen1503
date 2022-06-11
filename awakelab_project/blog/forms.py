from django import forms
from blog.models import Reclamo 

class ContactForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField(label='E-mail')
    categoria = forms.ChoiceField(choices= [('pregunta','Pregunta'), ('emergencia', 'Emergencia'), ('otros', 'Otros')])
    tema = forms.CharField(required=False)
    cuerpo = forms.CharField(widget=forms.Textarea)


class ReclamoForm(forms.ModelForm):
    class Meta:
        model = Reclamo
        fields = {'nombre', 'cuerpo'}