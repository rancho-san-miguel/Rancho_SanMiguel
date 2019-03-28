from django.urls import path
from .views import *
urlpatterns = [
    path('bovino/', Bovino_Create.as_view(), name="bovino_crear"),
    path('bovinolist/', Bovino_List.as_view(), name="bovino_list"),
    path('bovinoshow/<int:pk>', Bovino_Show.as_view(), name="bovino_show"),
    path('bovinoupdate/<int:pk>', Bovino_Update.as_view(), name="bovino_update"),
    path('bovinodelete/<int:pk>', Bovino_Delete.as_view(), name="bovino_delete"),
]