from django.urls import path
from .views import VRegistro,cerrar_sesion,loguear
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',VRegistro.as_view(),name="Autenticacion"),

    path('cerrar_sesion',cerrar_sesion,name="cerrar_sesion"),
    path('loguear',loguear,name="loguear"),

]


