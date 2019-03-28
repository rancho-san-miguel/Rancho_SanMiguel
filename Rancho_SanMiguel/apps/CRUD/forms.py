from django import forms
from .models import *


class Ganado_Form(forms.ModelForm):


    class Meta:
        model  = GANADO
        fields = {
            'nombre',
            'arete',
            'siniga',
            'sexo',
            'propietario',
            'ganadera',
            'no_padre',
            'no_madre',
            'fecha_nacimiento',
            'tipo_nacimiento',
            'tipo_parto',
            'tipo_servicio',
            'fecha_servicio',
            'localizacion_fierro',
            'potrero',
            'estado',
            'img',

        }
        labels = {
            'nombre':'nombre',
            'arete':'arete',
            'siniga':'siniga',
            'sexo':'sexo',
            'propietario':'propietario',
            'ganadera':'ganadera',
            'no_padre':'no_padre',
            'no_madre':'no_madre',
            'fecha_nacimiento':'fecha_nacimiento',
            'tipo_nacimiento':'tipo_nacimiento',
            'tipo_parto':'tipo_parto',
            'tipo_servicio':'tipo_sevicio',
            'fecha_servicio':'fecha_servicio',
            'localizacion_fierro':'localizacion_fierro',
            'potrero':'potrero',
            'estado':'estado',
            'img':'img',
        }


        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'arete': forms.TextInput(attrs={'class': 'form-control'}),
            'siniga': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo':forms.Select(attrs={'class': 'form-control'}),
            'propietario': forms.TextInput(attrs={'class': 'form-control'}),
            'ganadera': forms.TextInput(attrs={'class': 'form-control'}),
            'no_padre': forms.TextInput(attrs={'class': 'form-control'}),
            'no_madre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'tipo_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_parto': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_servicio': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'localizacion_fierro': forms.TextInput(attrs={'class': 'form-control'}),
            'potrero': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'img''img': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }