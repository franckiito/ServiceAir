# -*- coding: utf-8 -*-
from django import forms
from users.models import Usuario, TipoUsuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ['is_staff','is_superuser','last_login','date_joined','groups','user_permissions',]
        widgets = {
            'password': forms.PasswordInput(),
        }
    def save(self, commit=True): # Save the provided password in hashed format #
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
        return user

class LoginForm(forms.Form):

    usr = forms.CharField(label='Nombre de usuario')
    pwd = forms.CharField(label='Contraseña', widget=forms.PasswordInput())

class UsuarioFormSu(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = []
        widgets = {
            'password': forms.PasswordInput(),
        }

class TipoUsuarioForm(forms.ModelForm):
    class Meta:
        model = TipoUsuario
        exclude = []
        widgets = {
            'descripcion': forms.Textarea,
        }