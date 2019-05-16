from django.shortcuts import render
from .models import GANADO, BITACORA_GANADO, HISTORIAL_VENTAS_BOVINO, HISTORIAL_VENTAS_CERDOS, Notificaciones
from .models import REGISTRO_AGRICOLA, EN_PROCESO, EN_BODEGA, HISTORIAL_VENTAS_LECHE, HISTORIAL_VENTAS_CULTIVO

from .forms import Ganado_Form, Bitacora_Ganado_form, Ganado_Venta_form, Historial_Ventas_Bovino_form
from .forms import HISTORIAL_VENTAS_CERDOS, Notificaciones_form, Historial_Ventas_Cerdos_form
from .forms import Registro_Agricola_form, En_Proceso_form, En_Bodega_form, Historial_Ventas_Leche_form
from .forms import Historial_Ventas_Cultivo_form

from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from datetime import datetime



class Bovino_Create(CreateView):
    model = GANADO
    form_class = Ganado_Form
    template_name = 'RegBov/regbov_form.html'
    success_url = reverse_lazy('bovino_list')

class Bovino_List(ListView):
    # queryset = GANADO.objects.all()
    queryset = GANADO.objects.exclude(estado='Vendida').order_by('id')
    # queryset = GANADO.objects.exclude(estado='Vendida')
    template_name = 'RegBov/regbov_list.html'
    paginate_by = 5

class Bovino_Show(DetailView):
    model = GANADO
    template_name = 'RegBov/regbov_show.html'

class Bovino_Update(UpdateView):
    model = GANADO
    form_class = Ganado_Form
    template_name = 'RegBov/regbov_form.html'
    success_url = reverse_lazy('bovino_list')

def Bovino_edit(request, pk):
    print("Este es ek id: ",pk)
    query = GANADO.objects.get(id=pk)

    if request.method == 'POST':
        form2 = Bitacora_Ganado_form(request.POST)
        if form2.is_valid():
            form2.save()
    else:
        form2 = Bitacora_Ganado_form()

    if request.method == 'GET':
        form = Ganado_Form(instance=query)
    else:
        # form = Ganado_Venta_form(request.POST, instance=query)
        form = Ganado_Form(request.POST, instance=query)
        if form.is_valid():
            form.save()
        return redirect('bovino_list')

    dic = {
        'form':form,
        'form2':form2,
        }
    return render(request, 'RegBov/regbov_form.html', dic)


class Bovino_Delete(DeleteView):
    model = GANADO
    template_name = 'RegBov/regbov_delete.html'
    success_url = reverse_lazy('bovino_list')

def Bovino_Galeria_Venta_List(request):
    query = GANADO.objects.filter(galeria_venta=True).exclude(estado='Vendida').order_by('id')
    dic = {
        'object_list':query,
    }
    # return render(request, 'GaleriaVentas/calis.html', dic)
    return render(request, 'home/portfolio2.html', dic)

def Bovino_Galeria_Venta_Show(request,pk):
    query = GANADO.objects.get(pk=pk)
    dic = {
        'form':query,
    }
    return render(request, 'home/detalles.html', dic)
#---------------------------------------------------------------------------------------------------------------------
"""Bitacora ganado"""

class Bitacora_Create(CreateView):
    model = BITACORA_GANADO
    form_class = Bitacora_Ganado_form
    template_name = 'Bitacora/bitacora_form.html'
    success_url = reverse_lazy('bit_list')

class Bitacora_List(ListView):
    queryset = BITACORA_GANADO.objects.all()
    template_name = 'Bitacora/bitacora_list.html'
    paginate_by = 5

class Bitacora_Show(DetailView):
    model = BITACORA_GANADO
    template_name = 'Bitacora/bitacora_show.html'

class Bitacora_Update(UpdateView):
    model = BITACORA_GANADO
    form_class = Bitacora_Ganado_form
    template_name = 'Bitacora/bitacora_form.html'
    success_url = reverse_lazy('bit_list')


class Bitacora_Delete(DeleteView):
    model = BITACORA_GANADO
    template_name = 'Bitacora/bitacora_delete.html'
    success_url = reverse_lazy('bit_list')





#---------------------------------------------------------------------------------------------------------------------
"Venta de ganado"

def Bovino_update_ventas_create(request, pk):
    print("Este es el id: ",pk)
    query = GANADO.objects.get(pk=pk)

    "Create ventas"
    if request.method == 'POST':
        form2 = Historial_Ventas_Bovino_form(request.POST)
        if form2.is_valid():
            var = form2.save()

            # var.id_bovino = query.nombre
            var.id_bovino = pk
            var.save()

            query.estado = 'Vendida'
            query.save()


        return redirect('venta_list')
    else:
        form2 = Historial_Ventas_Bovino_form()

    "Update Ganado a venta"
    # if request.method == 'GET':
    #     form = Ganado_Form(instance=query)
    # else:
    #     # form = Ganado_Venta_form(request.POST, instance=query)
    #     form = Ganado_Form(request.POST, instance=query)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('bovino_list')

    dic = {
        'datos':query,
        # 'form':form,
        'form2':form2,
        }

    return render(request, 'RegBov/regbov_ventas_form.html', dic)



def Venta_Bovino_Show(request, pk):
    query1 = HISTORIAL_VENTAS_BOVINO.objects.get(pk=pk)
    query2 = GANADO.objects.get(pk=query1.id_bovino)
    dic = {
        'form1':query1,
        'form2':query2,
    }
    return render(request, 'Ventas/ventas_bovino_show.html', dic)



class Venta_Bovino_List(ListView):
    queryset = HISTORIAL_VENTAS_BOVINO.objects.all()
    # queryset = GANADO.objects.filter(estado='Vendida')
    template_name = 'Ventas/ventas_bovino_list.html'
    paginate_by = 5

class Venta_Bovino_Delete(DeleteView):
    model = HISTORIAL_VENTAS_BOVINO
    template_name = 'Ventas/ventas_bovino_delete.html'
    success_url = reverse_lazy('venta_list')


#---------------------------------------------------------------------------------------------------------------------
"Venta de cerdos"

class Venta_Cerdos_Create(CreateView):
    model = HISTORIAL_VENTAS_CERDOS
    form_class = Historial_Ventas_Cerdos_form
    template_name = 'Ventas/ventas_cerdos_form.html'
    success_url = reverse_lazy('cerdos_list')

class Venta_Cerdos_List(ListView):
    # queryset = HISTORIAL_VENTAS_CERDOS.objects.all()
    queryset = HISTORIAL_VENTAS_CERDOS.objects.exclude(estado=True).order_by('id')
    template_name = 'Ventas/ventas_cerdos_list.html'
    paginate_by = 5

def Venta_Cerdos_Delete(request, pk):
    query = HISTORIAL_VENTAS_CERDOS.objects.get(pk=pk)
    if request.method == 'POST':
        query.estado = True
        query.save()
        return redirect('cerdos_list')
    dic = {
        'form':query,
    }
    return render(request, 'Ventas/ventas_cerdos_delete.html', dic)
    #
    # if request.method == 'POST':
    #     form2 = Historial_Ventas_Bovino_form(request.POST)
    #     if form2.is_valid():
    #         var = form2.save()
    #
    #         # var.id_bovino = query.nombre
    #         var.id_bovino = pk
    #         var.save()
    #
    #         query.estado = 'Vendida'
    #         query.save()
    #
    #
    #     return redirect('venta_list')
    # else:
    #     form2 = Historial_Ventas_Bovino_form()


#---------------------------------------------------------------------------------------------------------------------
"Notificaciones"

def Notificaciones_function():
    ahora = datetime.now()
    return ahora

def Query_Notificaciones(request):
    Fecha_Actual = Notificaciones_function()

    day = Fecha_Actual.day
    month = Fecha_Actual.month
    year = Fecha_Actual.year

    if int(day) <= 9:
        day = "0"+str(day)

    if int(month) <= 9:
        month = "0"+str(month)

    var = str(year)+"-"+str(month)+"-"+str(day)

    query = Notificaciones.objects.filter(fecha=var)

    dic = {

        'form':query,
    }
    return render(request, 'Ventas/calis.html', dic)
    # return render(request, 'base/base.html',dic)

class Notificaciones_Create(CreateView):
    model = Notificaciones
    form_class = Notificaciones_form
    template_name = 'Notificaciones/notifi_form.html'
    success_url = reverse_lazy('index2')

#---------------------------------------------------------------------------------------------------------------------
"Agricola"
"CRUD del cultivo"
class Registro_Agricola_Create(CreateView):
    model = REGISTRO_AGRICOLA
    form_class = Registro_Agricola_form
    template_name = 'Cultivo/cultivo_form.html'
    success_url = reverse_lazy('cultivo_list')

class Registro_Agricola_List(ListView):
    queryset = REGISTRO_AGRICOLA.objects.all()
    template_name = 'Cultivo/cultivo_list.html'
    paginate_by = 5

class Registro_Agricola_Update(UpdateView):
    model = REGISTRO_AGRICOLA
    form_class = Registro_Agricola_form
    template_name = 'Cultivo/cultivo_form.html'
    success_url = reverse_lazy('cultivo_list')

class Registro_Agricola_Delete(DeleteView):
    model = REGISTRO_AGRICOLA
    template_name = 'Cultivo/cultivo_delete.html'
    success_url = reverse_lazy('cultivo_list')

"En proceso/que esta cultivado"
class En_Proceso_Create(CreateView):
    model = EN_PROCESO
    form_class = En_Proceso_form
    template_name = 'Cultivo/cultivo_en_proceso_form.html'
    success_url = reverse_lazy('cultivo_en_proceso_list')

class En_Proceso_List(ListView):
    queryset = EN_PROCESO.objects.all()
    template_name = 'Cultivo/cultivo_en_proceso_list.html'
    paginate_by = 5

class En_Proceso_Update(UpdateView):
    model = EN_PROCESO
    form_class = En_Proceso_form
    template_name = 'Cultivo/cultivo_en_proceso_form.html'
    success_url = reverse_lazy('cultivo_en_proceso_list')

class En_Proceso_Delete(DeleteView):
    model = EN_PROCESO
    template_name = 'Cultivo/cultivo_en_proceso_delete.html'
    success_url = reverse_lazy('cultivo_en_proceso_list')

class En_Proceso_Show(DetailView):
    model = EN_PROCESO
    template_name = 'Cultivo/cultivo_en_proceso_show.html'

"Almacen/Bodega"

def Create_Or_Update_En_Bodega(request, pk):
    query1 = EN_PROCESO.objects.get(pk=pk)
    query2 = EN_BODEGA.objects.get_or_create(producto=query1.producto, defaults={'producto':query1.producto,'cantidad':'0'})
    query3 = EN_BODEGA.objects.get(producto=query1.producto)
    # print("Mensaje------------------------------------------------------------------------")
    # print(query3.id)

    if request.method == 'POST':
        n1 = int(request.POST['numer1'])
        query3.cantidad = n1 + int(query3.cantidad)
        query3.save()

        query1.delete()

        return redirect('cultivo_en_proceso_list')

    dic = {
        'object':query1,
    }

    return render(request, 'Cultivo/cultivo_almacen_create.html', dic)

#
# class En_Proceso_List(ListView):
#     queryset = EN_PROCESO.objects.all()
#     template_name = 'Cultivo/cultivo_en_proceso_list.html'
#     paginate_by = 5

class En_Bodega_List(ListView):
    queryset = EN_BODEGA.objects.all()
    template_name = 'Cultivo/cultivo_almacen_list.html'
    paginate_by = 5

"Venta de lo que hay en bodega"
# class
def Venta_Cultivo(request, pk):
    query1 = EN_BODEGA.objects.get(pk=pk)
    print("Cantidad-----------------------------------------------------------------------------")
    print(query1.cantidad)
    if request.method == 'POST':
        form = Historial_Ventas_Cultivo_form(request.POST)
        if form.is_valid():
            var = form.save()
            var.producto = query1.producto
            query1.cantidad = int(query1.cantidad) - int(var.cantidad)
            query1.save()
            var.save()
        return redirect('almacen_list')
    else:
        form = Historial_Ventas_Cultivo_form()

    dic = {
        'form':query1,
        'form2':form,
    }

    return render(request, 'Ventas/Venta_Cultivo.html', dic)



class Venta_Cultivo_List(ListView):
    queryset = HISTORIAL_VENTAS_CULTIVO.objects.all()
    template_name = 'Ventas/ventas_cultivo_list.html'
paginate_by = 5



#---------------------------------------------------------------------------------------------------------------------
"Venta de leche"

class Venta_Leche_Create(CreateView):
    model = HISTORIAL_VENTAS_LECHE
    form_class = Historial_Ventas_Leche_form
    template_name = 'Ventas/ventas_leche_form.html'
    success_url = reverse_lazy('leche_list')

class Venta_Leche_List(ListView):
    # queryset = HISTORIAL_VENTAS_CERDOS.objects.all()
    queryset = HISTORIAL_VENTAS_LECHE.objects.exclude(estado=True).order_by('id')
    template_name = 'Ventas/ventas_leche_list.html'
    paginate_by = 5

def Venta_Leche_Delete(request, pk):
    query = HISTORIAL_VENTAS_LECHE.objects.get(pk=pk)
    if request.method == 'POST':
        query.estado = True
        query.save()
        return redirect('leche_list')
    dic = {
        'form':query,
    }
    return render(request, 'Ventas/ventas_leche_delete.html', dic)



