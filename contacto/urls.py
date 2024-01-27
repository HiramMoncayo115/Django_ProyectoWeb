from django.urls import path

from ProyectoWweb import views
from . import views

urlpatterns = [

    path('', views.contacto, name="Contacto")
]
