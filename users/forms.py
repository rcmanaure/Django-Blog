from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Formulario de registro costumizable.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model =User
        fields = ['username', 'email', 'password1', 'password2']

# Formulario para actualizar los datos del usuario.(Profile)
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model =User
        fields = ['username', 'email']

# Formulario para actualizar la foto del usuario(Profile)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
