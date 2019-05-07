from django.urls import path
from .views import Bovino_Create,Bovino_List, Bovino_Update, Bovino_Show, Bovino_Delete, Bovino_update_ventas_create
from .views import Bovino_Galeria_Venta_List, Bovino_Galeria_Venta_Show
from .views import Bitacora_Create, Bitacora_List, Bitacora_Show, Bitacora_Update, Bitacora_Delete
from .views import Venta_Bovino_List,Venta_Bovino_Delete, Venta_Bovino_Show
from .views import Venta_Cerdos_Create, Venta_Cerdos_List, Venta_Cerdos_Delete

from django.contrib.auth.decorators import login_required

from .views import Bovino_edit
urlpatterns = [
    #bovino
    path('bovino/', Bovino_Create.as_view(), name="bovino_crear"),
    path('bovinolist/', Bovino_List.as_view(), name="bovino_list"),
    path('bovino/galeria/venta/list/', Bovino_Galeria_Venta_List, name="bovino_galeria_venta_list"),
    path('bovino/galeria/venta/list/<int:pk>', Bovino_Galeria_Venta_Show, name="bovino_galeria_venta_show"),
    path('bovinoshow/<int:pk>', Bovino_Show.as_view(), name="bovino_show"),
    path('bovinoupdate/<int:pk>',Bovino_Update.as_view(), name="bovino_update"),
    path('bovinoventa/<int:pk>', Bovino_update_ventas_create, name="bovino_venta"),
    # path('bovinoupdate/<int:pk>', Bovino_edit, name="bovino_update"),
    path('bovinodelete/<int:pk>', Bovino_Delete.as_view(), name="bovino_delete"),
    #Bitacora
    path('bitacora/', Bitacora_Create.as_view(), name="bit_crear"),
    path('bitacoralist/', Bitacora_List.as_view(), name="bit_list"),
    path('bitacorashow/<int:pk>', Bitacora_Show.as_view(), name="bit_show"),
    path('bitacoraupdate/<int:pk>', Bitacora_Update.as_view(), name="bit_update"),
    path('bitacoradelete/<int:pk>', Bitacora_Delete.as_view(), name="bit_delete"),
    #Venta bovino
    path('ventalist/', Venta_Bovino_List.as_view(), name="venta_list"),
    path('ventadelete/<int:pk>', Venta_Bovino_Delete.as_view(), name="venta_delete"),
    path('ventashow/<int:pk>', Venta_Bovino_Show, name="venta_show"),
    #Venta de cerdos
    path('porcino/crear/', Venta_Cerdos_Create.as_view(), name="cerdos_crear"),
    path('porcino/list/', Venta_Cerdos_List.as_view(), name="cerdos_list"),
    path('porcino/delete/<int:pk>', Venta_Cerdos_Delete, name="cerdos_delete"),
]