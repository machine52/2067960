from home.models import *
from .serializer import *
from rest_framework import viewsets

# Create your views here.

class producto_viewset(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = producto_serializer

class marca_viewset(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = marca_serializer

class categoria_viewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = categoria_serializer

