from django.urls import path
from .views import GaleriaCreate, GaleriaList, GaleriaDelete, GaleriaDetail, GaleriaUpdate
from .views import GaleriaList2
from  .views import HistoriaCreate,HistoriaList,HistoriaDelete,HistoriaDetail,HistoriaUpdate

urlpatterns = [
    path('galeria/', GaleriaCreate.as_view(), name='galeria_create'),
    path('galerialist/', GaleriaList.as_view(), name='galeria_list'),
    path('galeriadelete/<int:pk>/', GaleriaDelete.as_view(), name='galeria_delete'),
    path('galeriashow/<int:pk>/', GaleriaDetail.as_view(), name='galeria_show'),
    path('galeriaupdate/<int:pk>/', GaleriaUpdate.as_view(), name='galeria_update'),
    path('galerialist2/', GaleriaList2.as_view(), name='galeria_list2'),



    path('historia/', HistoriaCreate.as_view(), name='Historial_Compras_create'),
    path('historialist/', HistoriaList.as_view(), name='Historial_Compras_list'),
    path('historiadelete/<int:pk>/', HistoriaDelete.as_view(), name='Historial_Compras_delete'),
    path('historiahow/<int:pk>/', HistoriaDetail.as_view(), name='Historial_Compras_show'),
    path('historiaupdate/<int:pk>/', HistoriaUpdate.as_view(), name='Historial_Compras_update'),
]