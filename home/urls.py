from django.urls import path
from .views import *

urlpatterns = [
    path('', about_view, name='about_view'),
    path('contacto/', contacto_view, name='contacto_view'),
    path('servicios/', servicios_view, name='servicios_view'),

    path('productos/', productos_view, name='productos_view'),
    path('agregar_producto/', agregar_producto_view, name='agregar_producto'),
    path('agregar_marca/', agregar_marca_view, name='agregar_marca'),
    path('agregar_categoria/', agregar_categoria_view, name='agregar_categoria'),
    path('ver_producto/<int:id_prod>', ver_producto_view, name='ver_producto'),
    
]