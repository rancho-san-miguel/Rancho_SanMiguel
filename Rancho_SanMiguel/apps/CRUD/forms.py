from django import forms
from .models import GANADO, BITACORA_GANADO, HISTORIAL_VENTAS_BOVINO, HISTORIAL_VENTAS_CERDOS, Notificaciones
from .models import REGISTRO_AGRICOLA, EN_PROCESO, EN_BODEGA, HISTORIAL_VENTAS_LECHE, HISTORIAL_VENTAS_CULTIVO
from .models import CULTIVO_ALMACEN_BAJA, CONTROL_GANADO, GANADO_BITACORA
from django.forms.widgets import SelectDateWidget

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


import datetime

y = datetime.datetime.now()

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
        model = GANADO
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
            'peso',
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
            'peso':'Peso de nacimiento',
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
            'no_padre': forms.TextInput(attrs={'class': 'form-control'}),
            'no_madre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
            'tipo_nacimiento': forms.Select(attrs={'class': 'form-control'}),
            'tipo_parto': forms.Select(attrs={'class': 'form-control'}),
            'localizacion_fierro': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame la localización del fierro'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'peso':forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el peso, Ej. 120.5'}),
            'galeria_venta': forms.CheckboxInput(),
            'img''img': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }


class Ganado_Bitacora_Form(forms.ModelForm):
    # fecha_nacimiento=forms.DateTimeField(input_formats=['%d/%m/%Y'])
    class Meta:

        model = GANADO
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
            'peso',
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
            'peso':'Peso de nacimiento',
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
            'fecha_nacimiento': forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
            'tipo_nacimiento': forms.Select(attrs={'class': 'form-control'}),
            'tipo_parto': forms.Select(attrs={'class': 'form-control'}),
            'localizacion_fierro': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame la localización del fierro'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
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
            'fecha': forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
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
            'fecha': forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
        }

class Notificaciones_form(forms.ModelForm):
    class Meta:
        model = Notificaciones
        fields = {
            'descripcion',
            'fecha',
        }
        labels = {
            'descripcion':'Descripción',
            'fecha':'Fecha del evento',
        }
        widgets = {
            'descripcion':forms.Textarea(attrs={'class': 'form-control','placeholder':'Descripción de las actividades a realizar'}),
            'fecha':forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }

class Registro_Agricola_form(forms.ModelForm):
    class Meta:
        model = REGISTRO_AGRICOLA
        fields = {
            'producto',
        }
        labels = {
            'producto':'Producto',
        }
        widgets = {
            'producto':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre del producto Ej. Maíz, Frijol'}),
        }

class Control_ganado_form(forms.ModelForm):
    class Meta:
        model = CONTROL_GANADO
        fields = {
            'arete',
            'motivo',
            'descripcion',
            'lugar',
            'fecha',
        }
        labels = {
            'arete':'Arete',
            'motivo': 'Motivo',
            'descripcion':'Descripción',
            'lugar':'Lugar',
            'fecha':'Fecha',
        }
        widgets = {
            'arete': forms.TextInput(attrs={'class': 'form-control'}),
            'motivo': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
        }

class En_Proceso_form(forms.ModelForm):
    class Meta:
        model = EN_PROCESO
        fields = {
            'producto',
            'hectareas',
            'cantidad',
            'pe',
        }
        labels = {
            'producto': 'Producto',
            'hectareas':'Hectáreas a producir',
            'cantidad':'Cantidad',
            'pe':'Producción estimada',
        }
        widgets = {
            'producto':forms.Select(attrs={'class': 'form-control'}),
            'hectareas':forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame las hectáreas Ej. 5'}),
            'cantidad':forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame la cantidad Ej. 12000'}),
            'pe':forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame la producción estimada '}),
        }

class En_Bodega_form(forms.ModelForm):
    class Meta:
        model = EN_BODEGA
        fields = {
            # 'producto',
            # 'hectareas',
            'cantidad',
            # 'pe',
        }
        labels = {
            # 'producto': 'Producto',
            # 'hectareas': 'Hectareas a producir',
            'cantidad': 'Cantidad',
            # 'pe': 'P.E',
        }
        widgets = {
            # 'producto': forms.Select(attrs={'class': 'form-control'}),
            # 'hectareas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dame las hectareas Ej. 5'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dame la cantidad final'}),
            # 'pe': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dame el P.E'}),
        }


class Historial_Ventas_Leche_form(forms.ModelForm):
    class Meta:
        model = HISTORIAL_VENTAS_LECHE
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
            'cantidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cantidad Litros de Leche'}),
            'total': forms.TextInput(attrs={'class': 'form-control','placeholder':'Costo ejemplo: 15.20'}),
            'fecha': forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
        }

class Historial_Ventas_Cultivo_form(forms.ModelForm):
    class Meta:
        model = HISTORIAL_VENTAS_CULTIVO
        fields = {
            # 'producto',
            'cantidad',
            'total',
            'fecha',
        }
        labels = {
            # 'producto':"Producto",
            'cantidad':'Cantidad',
            'total':'Total',
            'fecha':'Fecha',
        }
        widgets = {
            # 'producto': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cantidad Litros de Leche'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cantidad a vender'}),
            'total': forms.TextInput(attrs={'class': 'form-control','placeholder':'Costo total'}),
            'fecha': forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
        }

class Cultivo_Almacen_Baja_form(forms.ModelForm):
    class Meta:
        model = CULTIVO_ALMACEN_BAJA
        fields = {
            # 'producto',
            'cantidad',
            'descripcion',
        }
        labels = {
            # 'producto',
            'cantidad':'Cantidad',
            'descripcion':'Descripción',
        }
        widgets = {
            # 'producto',
            'cantidad':forms.TextInput(attrs={'class': 'form-control','placeholder':'Cantidad a dar de bajar'}),
            'descripcion':forms.Textarea(attrs={'class': 'form-control','placeholder':'Motivo por el cual se esta dando de baja'}),
        }
#
# class SignUpForm(UserCreationForm):
#     username = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
#     first_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),max_length=32, help_text='First name')
#     last_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),max_length=32, help_text='Last name')
#     email = forms.EmailField(forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64,help_text='Enter a valid email address')
#     password1 = forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
#     password2 = forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))
#     class Meta(UserCreationForm):
#         model = User
#         fields = UserCreationForm.Meta.fields + ('first_name','last_name','email')

class SignUpForm(UserCreationForm):
    # password1 = forms.CharField()
    # password2 = forms.CharField()
    class Meta(UserCreationForm):
        model = User

        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email')
        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            # 'username':forms.CharField(help_text='First name'),
            'first_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'email':forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electronico'}),
            'password1' : forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
            'password2':forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña otra vez'}),
        }

