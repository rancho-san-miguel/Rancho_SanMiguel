from django.db import models
from model_utils import Choices
from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save

class GANADO(models.Model):
    opciones = Choices('Macho','Hembra')
    opciones2 = Choices('Vendida','Viva','Muerta')
    nombre = models.CharField(max_length=15)
    arete= models.CharField(max_length=10)
    siniga = models.CharField(max_length=10)
    sexo = estado = models.CharField(choices=opciones, max_length=10)
    propietario = models.CharField(max_length=20)
    ganadera = models.CharField(max_length=20)
    no_padre = models.IntegerField()
    no_madre = models.IntegerField()
    fecha_nacimiento = models.DateTimeField()
    tipo_nacimiento= models.DateTimeField()
    tipo_parto= models.CharField(max_length=1)
    tipo_servicio= models.CharField(max_length=1)
    fecha_servicio= models.DateTimeField()
    localizacion_fierro = models.CharField(max_length=10)
    potrero= models.CharField(max_length=1)
    estado = models.CharField(choices=opciones2, max_length=10)
    img = models.ImageField(verbose_name="Imagen", upload_to='Galeria')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.nombre

# Borrar la foto vieja si se le da al boton borrar
@receiver(post_delete, sender=GANADO)
def photo_post_delete_handler(sender, **kwargs):
    listiningImage = kwargs['instance']
    storage, path = listiningImage.img.storage, listiningImage.img.path
    storage.delete(path)

# Borrar la foro vieja si se actualiza
@receiver(pre_save, sender=GANADO)
def update_img(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_img = GANADO.objects.get(pk=instance.pk).img
        except:
            return
        else:
            new_img = instance.img
            if old_img and old_img.url != new_img.url:
                old_img.delete(save=False)

class BITACORA_GANADO(models.Model):
    arete = models.CharField(max_length=10)
    lugar = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.arete

class CONTROL_GANADO(models.Model):
    arete = models.CharField(max_length=10)
    motivo = models.CharField(max_length=30)
    descripcion = models.TextField()
    lugar = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.arete

class HISTORIAL_VENTAS(models.Model):
    tipo = models.CharField(max_length=30)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    total = models.FloatField()
    fecha = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.id

class INVENTARIO(models.Model):
    opciones = Choices('Porciono','Agricola','Bovino')
    producto = models.CharField(max_length=30)
    tipo = models.CharField(choices=opciones, max_length=10)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.producto

class INGRESOS(models.Model):
    motivo = models.CharField(max_length=30)
    monto = models.FloatField()
    fecha = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.motivo


class PRODUCCION(models.Model):
    opciones = Choices('Toneladas','Pacas')
    producto = models.CharField(max_length=30)
    produccion = models.FloatField()
    medida = models.CharField(choices=opciones, max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.producto

class GASTOS(models.Model):
    opciones = Choices('Bovino','Porciono','Agricola')
    tipo = models.CharField(choices=opciones, max_length=10)
    motivo = models.CharField(max_length=30)
    monto = models.FloatField()
    fecha = models.DateTimeField()
    img = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.id

class DEUDORES_ACREEDORES(models.Model):
    opciones = Choices('Deudor','Acreedor')
    tipo = models.CharField(choices=opciones, max_length=10)
    motivo = models.CharField(max_length=30)
    monto = models.FloatField()
    fecha = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.id

class PLAN_CERDOS(models.Model):
    no_plan = models.IntegerField()
    cerdos = models.IntegerField()
    lechones = models.IntegerField()
    precio = models.FloatField()

    class Meta:
        ordering = ["id"]
    def __str__(self):
        return self.no_plan

class PLAN_AGRICOLA(models.Model):
    opciones = Choices('Toneladas', 'Pacas')
    no_plan = models.IntegerField()
    tipo_plan = models.CharField(max_length=30)
    cultivo = models.IntegerField()
    unidad_medida = models.CharField(choices=opciones, max_length=10)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]
    def __str__(self):
        return self.no_plan

class PLAN_LECHE(models.Model):
    no_plan = models.IntegerField()
    vacas_produccion = models.CharField(max_length=30)
    produccion_promedio = models.IntegerField()
    ingreso_diario = models.FloatField()
    estimado_anual = models.FloatField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.no_plan

class PROYECCION_GASTOS(models.Model):
    tipo_gasto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    cantidad = models.FloatField()
    total = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]
    def __str__(self):
        return self.id

class PLAN_BOVINO(models.Model):
    no_plan = models.IntegerField()
    tipo_ganado = models.CharField(max_length=30)
    hato = models.IntegerField()
    venta = models.FloatField()
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.no_plan
