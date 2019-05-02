from django.contrib import admin

from .models import *


# class inventario(admin.ModelAdmin):
#      readonly_fields = ('id', 'created', 'updated')

class ganado(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

class bitacora(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

# class bitacora(admin.ModelAdmin):
#      readonly_fields = ('id', 'created', 'updated')

admin.site.register(BITACORA_GANADO, bitacora)
# admin.site.register(GANADO, ganado)
# admin.site.register(INVENTARIO, inventario)
# admin.site.register(BITACORA_GANADO, bitacora)
# Register your models here.
