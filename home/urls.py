from django.urls import path
from .views import *

urlpatterns = [
    path('', about_view, name='about_view'),
    path('contacto/', contacto_view, name='contacto_view'),
    path('servicios/', servicios_view, name='servicios_view'),
]