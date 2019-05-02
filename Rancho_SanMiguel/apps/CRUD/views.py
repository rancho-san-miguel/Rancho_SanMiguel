from django.shortcuts import render
from .models import GANADO, BITACORA_GANADO
from .forms import Ganado_Form, Bitacora_Ganado_form, Ganado_Venta_form

from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView


class Bovino_Create(CreateView):
    model = GANADO
    form_class = Ganado_Form
    template_name = 'RegBov/regbov_form.html'
    success_url = reverse_lazy('bovino_list')

class Bovino_List(ListView):
    queryset = GANADO.objects.all()
    # queryset = GANADO.objects.exclude(estado='Vendida').order_by(id)
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
# def Venta_Ganado(request):
#     if  request.method == 'POST':
#         form = Historial_Ventas_form
#         if form.is_valid():







