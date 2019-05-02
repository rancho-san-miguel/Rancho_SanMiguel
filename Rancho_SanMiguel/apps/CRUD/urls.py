from django.urls import path
from .views import Bovino_Create,Bovino_List, Bovino_Update, Bovino_Show, Bovino_Delete
from .views import Bitacora_Create, Bitacora_List, Bitacora_Show, Bitacora_Update, Bitacora_Delete

from django.contrib.auth.decorators import login_required

from .views import Bovino_edit
urlpatterns = [
    path('bovino/', Bovino_Create.as_view(), name="bovino_crear"),
    path('bovinolist/', Bovino_List.as_view(), name="bovino_list"),
    path('bovinoshow/<int:pk>', Bovino_Show.as_view(), name="bovino_show"),
    path('bovinoupdate/<int:pk>',Bovino_Update.as_view(), name="bovino_update"),
    # path('bovinoupdate/<int:pk>', Bovino_edit, name="bovino_update"),
    path('bovinodelete/<int:pk>', Bovino_Delete.as_view(), name="bovino_delete"),
    #Bitacora
    path('bitacora/', Bitacora_Create.as_view(), name="bit_crear"),
    path('bitacoralist/', Bitacora_List.as_view(), name="bit_list"),
    path('bitacorashow/<int:pk>', Bitacora_Show.as_view(), name="bit_show"),
    path('bitacoraupdate/<int:pk>', Bitacora_Update.as_view(), name="bit_update"),
    path('bitacoradelete/<int:pk>', Bitacora_Delete.as_view(), name="bit_delete"),
    #Venta bovino

]