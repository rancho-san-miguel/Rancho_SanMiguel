from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save


class Galeria(models.Model):
    nombre = models.CharField(max_length=40, null=True, blank=True)
    img = models.ImageField(verbose_name="Imagen", upload_to='Galeria')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        ordering = ["-updated"]

    def __str__(self):
        return self.nombre

class Historial(models.Model):
    descripcion = models.CharField(max_length=40, null=True, blank=True)
    total = models.CharField(max_length=40, null=True, blank=True)
    fecha = models.DateField()
    img = models.ImageField(verbose_name="Imagen", upload_to='Galeria')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        ordering = ["-updated"]

    def __str__(self):
        return self.descripcion

# Borrar la foto vieja si se le da al boton borrar
@receiver(post_delete, sender=Galeria)
def photo_post_delete_handler(sender, **kwargs):
    listiningImage = kwargs['instance']
    storage, path = listiningImage.img.storage, listiningImage.img.path
    storage.delete(path)

# Borrar la foro vieja si se actualiza
@receiver(pre_save, sender=Galeria)
def update_img(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_img = Galeria.objects.get(pk=instance.pk).img
        except:
            return
        else:
            new_img = instance.img
            if old_img and old_img.url != new_img.url:
                old_img.delete(save=False)

