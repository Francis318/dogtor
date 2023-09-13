from django import forms

#Los formularios se tienen que vincular con los modelos
#importamos los modelos
from .models import PetOwner, Pet
#Los formularios se representan como clases

class OwnerForm(forms.ModelForm):
    #1.modelo de nuestro formulario
    #2.los fields que van a estar en nuestro formulario
    class Meta:
        model=PetOwner
        fields=("first_name","last_name","address","email","phone")


class PetForm(forms.ModelForm):
    #1.modelo de nuestro formulario
    #2.los fields que van a estar en nuestro formulario
    class Meta:
        model=Pet
        fields=("name","type","owner")