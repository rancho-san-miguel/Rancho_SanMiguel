from django.shortcuts import render
from itertools import chain
from .models import *
from .forms import Ganado_Form

from django.urls import reverse_lazy
from django.contrib.auth.admin import User

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

class Bovino_Create(CreateView):
    model = GANADO
    form_class = Ganado_Form
    template_name = 'RegBov/regbov_form.html'
    success_url = reverse_lazy('bovino_list')

class Bovino_List(ListView):
    queryset = GANADO.objects.order_by('id')
    # queryset2 = INVENTARIO.objects.order_by('id')
    # result_list = list(chain(queryset, queryset2))
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

class Bovino_Delete(DeleteView):
    model = GANADO
    template_name = 'RegBov/regbov_delete.html'
    success_url = reverse_lazy('bovino_list')

# Create your views here.
