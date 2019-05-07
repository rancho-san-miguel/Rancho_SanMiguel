from django import forms
from .models import GANADO, BITACORA_GANADO, HISTORIAL_VENTAS_BOVINO, HISTORIAL_VENTAS_CERDOS
from django.forms.widgets import SelectDateWidget


class Ganado_Venta_form(forms.ModelForm):
    class Meta:
        model = GANADO
        fields = {
            'estado'
        }
        labels = {
            'estado':'Estado'
        }
        widgets = {
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }


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
            'localizacion_fierro',
            'estado',
            'galeria_venta',
            'img',

        }
        labels = {
            'nombre':'Nombre',
            'arete':'Arete',
            'siniga':'Siniga',
            'sexo':'Sexo',
            'propietario':'Propietario',
            'ganadera':'Ganadera',
            'no_padre':'Número del padre',
            'no_madre':'Número de la madre',
            'fecha_nacimiento':'Fecha de nacimiento',
            'tipo_nacimiento':'Tipo de nacimiento',
            'tipo_parto':'Tipo de parto',
            'localizacion_fierro':'Fierro',
            'estado':'Estado',
            'galeria_venta':'Ponerlo a la venta en la galeria',
            'img':'Foto',
        }


        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el nombre del bovino'}),
            'arete': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el codigo del arete del bovino'}),
            'siniga': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame la siniga del bovino'}),
            'sexo':forms.Select(attrs={'class': 'form-control'}),
            'propietario': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre del propietario del bovino'}),
            'ganadera': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ganadera'}),
            'no_padre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el número del padre'}),
            'no_madre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el número de la madre'}),
            'fecha_nacimiento': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
            'tipo_nacimiento': forms.Select(attrs={'class': 'form-control'}),
            'tipo_parto': forms.Select(attrs={'class': 'form-control'}),
            'localizacion_fierro': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame la localización del fierro'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'galeria_venta': forms.CheckboxInput(),
            'img''img': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }

class Bitacora_Ganado_form(forms.ModelForm):
    class Meta:
        model = BITACORA_GANADO
        fields = {
            'bovino',
            'descripcion',
            'lugar',
            'fecha',
        }
        labels = {
            'bovino':'Bovino',
            'descripcion':'Descripcion',
            'lugar':'Lugar',
            'fecha':'Fecha',
        }
        widgets = {
            # 'bovino': forms.TextInput(attrs={'class': 'form-control'}),
            'bovino': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }

class Historial_Ventas_Bovino_form(forms.ModelForm):
    class Meta:
        model = HISTORIAL_VENTAS_BOVINO
        fields = {
            # 'id_bovino',
            'descripcion',
            'total',
            'fecha',
        }
        labels = {
            # 'id_bovino':'Id del bovino',
            'descripcion':'Descripción',
            'total':'Costo total',
            'fecha':'Fecha de la venta',
        }
        widgets = {
            'descripcion':forms.Textarea(attrs={'class': 'form-control','placeholder':'Descripción de la venta'}),
            'total': forms.TextInput(attrs={'class': 'form-control','placeholder':'Costo ejemplo: 250.70'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }

class Historial_Ventas_Cerdos_form(forms.ModelForm):
    class Meta:
        model = HISTORIAL_VENTAS_CERDOS
        fields = {
            'cantidad',
            'total',
            'fecha',
        }
        labels = {
            'cantidad':'Cantidad',
            'total':'Total',
            'fecha':'Fecha',
        }
        widgets = {
            'cantidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cantidad cerdos'}),
            'total': forms.TextInput(attrs={'class': 'form-control','placeholder':'Costo ejemplo: 250.70'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }


# class Historial_Ventas_form(forms.ModelForm):
#     class Meta:
#         model = HISTORIAL_VENTAS
#         fields = {
#             'tipo',
#             'descripcion',
#             'cantidad',
#             'total',
#             'fecha',
#         }
#         labels = {
#             'tipo':'Tipo de venta',
#             'descripcion':'Descripción',
#             'cantidad':'Cantidad',
#             'total':'Total',
#             'fecha':'Fecha de la venta',
#         }
#         widgets = {
#             'tipo': forms.Select(attrs={'class': 'form-control'}),
#             'descripcion': forms.Textarea(attrs={'class': 'form-control','placeholder':'Descripcion del producto'}),
#             'cantidad': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
#             'total': forms.TextInput(attrs={'class': 'form-control'}),
#             'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
#         }
#
