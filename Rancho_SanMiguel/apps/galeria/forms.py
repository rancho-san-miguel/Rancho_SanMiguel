
from django import forms

from .models import Galeria,Historial

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = {
            'nombre',
            'img',
        }

        labels = {
            'nombre': 'Nombre',
            'img': 'Imagen',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Titulo de la imagen'}),
            'img': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }

class HistorialForm(forms.ModelForm):
    class Meta:
        model = Historial
        fields = {
            'descripcion',
            'total',
            'fecha',
            'img',
        }

        labels = {
            'descripcion': 'Descripcion',
            'total': 'Total',
            'fecha': 'Fecha',
            'img': 'Imagen',
            }

        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion de la compra'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total de la compra'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            }