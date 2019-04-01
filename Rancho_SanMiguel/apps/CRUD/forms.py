from django import forms
from .models import *
from django.forms.widgets import SelectDateWidget


class Ganado_Form(forms.ModelForm):
    # fecha_nacimiento=forms.DateTimeField(input_formats=['%d/%m/%Y'])
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
            # 'tipo_servicio',
            # 'fecha_servicio',
            'localizacion_fierro',
            # 'potrero',
            'estado',
            # 'img',

        }
        labels = {
            'nombre':'Nombre',
            'arete':'Arete',
            'siniga':'Siniga',
            'sexo':'Sexo',
            'propietario':'Propietario',
            'ganadera':'Ganadera',
            'no_padre':'Numero del padre',
            'no_madre':'Numero de la madre',
            'fecha_nacimiento':'Fecha de nacimiento',
            'tipo_nacimiento':'Tipo de nacimiento',
            'tipo_parto':'Tipo de parto',
            # 'tipo_servicio':'Tipo de servicio',
            # 'fecha_servicio':'Fecha de servicio',
            'localizacion_fierro':'Localizacion de fierro',
            # 'potrero':'Potrero',
            'estado':'Estado',
            # 'img':'Foto',
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
            'fecha_nacimiento': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
            # 'fecha_nacimiento': forms.DateTimeInput(attrs={'class':'vDateField','id':'id_fecha_nacimiento_0'}),
            'tipo_nacimiento': forms.Select(attrs={'class': 'form-control'}),
            'tipo_parto': forms.Select(attrs={'class': 'form-control'}),
            # 'tipo_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            # 'fecha_servicio': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'localizacion_fierro': forms.TextInput(attrs={'class': 'form-control'}),
            # 'potrero': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            # 'img''img': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }