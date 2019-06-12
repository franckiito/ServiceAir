# -*- coding: utf-8 -*-
from django import forms
from producto.models import Bodega, TipoFuncionamiento, Producto, TipoRepuesto, Repuesto

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        exclude = []
        widgets = {
            'descripcion': forms.Textarea,
        }

class TipoFuncionamientoForm(forms.ModelForm):
    class Meta:
        model = TipoFuncionamiento
        exclude = []
        widgets = {
            'descripcion': forms.Textarea,
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = []
        widgets = {
            'descripcion': forms.Textarea,
        }

class TipoRepuestoForm(forms.ModelForm):
    class Meta:
        model = TipoRepuesto
        exclude = []
        widgets = {
            'descripcion': forms.Textarea,
        }

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        exclude = []
        widgets = {
            'descripcion': forms.Textarea,
        }