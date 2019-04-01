from django.shortcuts import render
from .models import GANADO
from .forms import Ganado_Form

from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView


class Bovino_Create(CreateView):
    model = GANADO
    form_class = Ganado_Form
    template_name = 'RegBov/regbov_form.html'
    success_url = reverse_lazy('bovino_list')

class Bovino_List(ListView):
    queryset = GANADO.objects.all()
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

