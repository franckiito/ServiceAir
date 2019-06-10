# -*- coding: utf-8 -*-
from django import forms
from producto.models import Bodega, TipoFuncionamiento, Producto, TipoRepuesto, Repuesto

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        exclude = []
        widgets = {
            
        }

class TipoFuncionamientoForm(forms.ModelForm):
    class Meta:
        model = TipoFuncionamiento
        exclude = []
        widgets = {
            
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = []
        widgets = {
            
        }

class TipoRepuestoForm(forms.ModelForm):
    class Meta:
        model = TipoRepuesto
        exclude = []
        widgets = {
            
        }

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        exclude = []
        widgets = {
            
        }