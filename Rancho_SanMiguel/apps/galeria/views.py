from django.shortcuts import render


from .models import Galeria,Historial
from .forms import GaleriaForm,HistorialForm
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy

# Create your views here.

"Galeria------------------------------------------------------------------------------------"
class GaleriaCreate(CreateView):
    model = Galeria
    form_class = GaleriaForm
    template_name = 'Galeria/galeria_form.html'
    success_url = reverse_lazy('galeria_list')

class GaleriaList(ListView):
    queryset = Galeria.objects.all()
    template_name = 'Galeria/galeria_list.html'
    paginate_by = 5

class GaleriaDetail(DetailView):
    model = Galeria
    template_name = 'Galeria/galeria_show.html'

class GaleriaDelete(DeleteView):
    model = Galeria
    template_name =  'Galeria/galeria_delete.html'
    success_url = reverse_lazy('galeria_list')

class GaleriaUpdate(UpdateView):
    model = Galeria
    form_class = GaleriaForm
    template_name = 'Galeria/galeria_form.html'
    success_url = reverse_lazy('galeria_list')

class GaleriaList2(ListView):
    queryset = Galeria.objects.all()
    template_name = 'home/portfolio.html'



"Historial------------------------------------------------------------------------------------"
class HistoriaCreate(CreateView):
    model = Historial
    form_class = HistorialForm
    template_name = 'Historial_Compras/Historial_Compras_form.html'
    success_url = reverse_lazy('index2')

class HistoriaList(ListView):
    queryset = Historial.objects.all()
    template_name = 'Historial_Compras/Historial_Compras_list.html'
    paginate_by = 5

class HistoriaDetail(DetailView):
    model = Historial
    template_name = 'Historial_Compras/Historial_Compras_show.html'

class HistoriaDelete(DeleteView):
    model = Historial
    template_name =  'Historial_Compras/Historial_Compras_delete.html'
    success_url = reverse_lazy('index2')

class HistoriaUpdate(UpdateView):
    model = Historial
    form_class = HistorialForm
    template_name = 'Historial_Compras/Historial_Compras_form.html'
    success_url = reverse_lazy('index2')