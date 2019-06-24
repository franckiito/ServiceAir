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
            'image': forms.FileInput,
        }

class TipoRepuestoForm(forms.ModelForm):
    class Meta:
        model = TipoRepuesto
        exclude = []
        labels = { 'nombre': 'Nombre tipo Repuesto', 'descripcion': 'Describe el tipo de repuesto',}
        help_texts = { 'nombre': 'Ingrese nombre del nuevo tipo de repuesto',
                       'descripcion': 'ingrese una descripcion para el nuevo tipo de repuesto', }
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
