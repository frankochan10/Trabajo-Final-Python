from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

class FormularioPerfilUsuario(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=False, label="Nombre")
    last_name = forms.CharField(max_length=50, required=False, label="Apellido")
    email = forms.EmailField(required=True, label="Correo Electrónico")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class FormularioPerfilAvatar(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('avatar', 'biografia')