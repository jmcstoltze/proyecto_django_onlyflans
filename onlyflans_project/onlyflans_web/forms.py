
''' Corresponde al uso de 'form'
from django import forms

class ContactFormForm(forms.Form):

    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')
    '''

# Corresponde al uso de ModelForm
from django.forms import ModelForm
from .models import ContactForm  # Importa el modelo ContactForm

class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message']
