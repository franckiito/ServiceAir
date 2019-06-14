# -*- coding: utf-8 -*-
from django import forms
from servicios.models import TipoServicio, Solicitud, Agendamiento

class TipoServicioForm(forms.ModelForm):
    class Meta:
        model = TipoServicio
        exclude = []
        widgets = {
            'descripcion': forms.Textarea,
        }

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        exclude = []
        widgets = {
            'descripcion': forms.Textarea,
        }

class AgendamientoForm(forms.ModelForm):
    class Meta:
        model = Agendamiento
        exclude = []
        widgets = {
            'descripcion': forms.Textarea,
        }